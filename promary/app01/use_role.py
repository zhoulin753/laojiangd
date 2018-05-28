from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import *


class use_role(object):
    def process_request(self, request):
        if request.method == 'POST':
            use = authenticate(username=request.POST.get('name'), password=request.POST.get('password'))
            if not use:
                return render(request, 'index.html')
            else:
                login(request, use)
                role_list = Userinfo.objects.get(name=request.user.username).role.all()
                request.session['role'] = str(role_list)
                competence_list = []
                for i in role_list:
                    # 权限加到列表中
                    competence_list.append(i.competence.all())

                menu_list = Menu.objects.all().values()
                menu_dict = {}
                for i in menu_list:
                    i['children'] = []
                    menu_dict[i['id']] = i
                for i in range(len(menu_list)):
                    if menu_dict[i + 1]['menus_id']:
                        menu_dict[menu_dict[i + 1]['menus_id']]['children'].append(menu_dict[i + 1])
                        menu_dict.pop(i + 1)

                menu = []
                for i in menu_dict:
                    menu.append(menu_dict[i])

                def func(menu):
                    a = '<div>{0}{1}</div>'
                    b = '<a>{0}</a>'
                    html = ''
                    for i in menu:

                        if i['children']:
                            html += a.format(i['name'], func(i['children']))
                        else:
                            html += b.format(i['name'])
                    return html

                html = func(menu)
                print(menu)
                print('hatme', func(menu))
                return render(request, 'use_role.html', locals())
