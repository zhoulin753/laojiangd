from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from django import db

from .usermodelform import *


def index(request):
    # if request.method == 'POST':
    #     use = authenticate(username=request.POST.get('name'),password=request.POST.get('password'))
    #     if not use:
    #         return render(request, 'index.html')
    #     else:
    #         login(request,use)
    #         role_list = Userinfo.objects.get(name=request.user.username).role.values()
    #         request.session['role']=role_list
    #         return render(request, 'use_role.html')
    return render(request, 'index.html')


def use(request):
    use_list = Userinfo.objects.all()
    print(use_list)
    return render(request, 'user.html', locals())


def log_in(request):
    user = Usermodelform()
    if request.method == 'GET':
        user = Usermodelform(request.GET)
        if user.is_valid():
            user.save()
        else:
            if request.path == '/login/':
                user = Usermodelform(data=request.GET)
                print(request.GET)
                return render(request, 'log_in.html', locals())
            else:
                import re
                username = re.match(r'/login/(\w+)', request.path)
                if username:
                    username = re.match(r'/login/(\w+)', request.path).group(1)
                    use = Userinfo.objects.filter(name=username)
                    u = use.values().first()
                    user = Usermodelform(data=u)
                    use.delete()
                    return render(request, 'log_in.html', locals())
                else:
                    username = re.match(r'/login/%(\w+)%', request.path)
                    u = Userinfo.objects.filter(name=username.group(1))
                    u.delete()
                    return redirect('/use/')
            # return render(request, 'login.html', locals())
        return redirect('/use/')
