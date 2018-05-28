from django.db import models


# Create your models here.
class Userinfo(models.Model):
    name = models.CharField(max_length=10, null=True, unique=True)
    phone = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=15)
    email = models.EmailField(max_length=20)
    role = models.ManyToManyField('Role', blank=True, null=True)

    # role = models.ForeignKey('Role',blank=None,null=True,)
    def __str__(self):
        return self.name


class Role(models.Model):
    # 角色
    title = models.CharField(max_length=20)
    competence = models.ManyToManyField('Competence')

    # menu = models.ForeignKey('Competence')
    def __str__(self):
        return self.title


class Menu(models.Model):
    # 菜单
    name = models.CharField(max_length=10, null=False)
    menus = models.ForeignKey('Menu', blank=True, null=True)

    def __str__(self):
        return self.name


class Competence(models.Model):
    # 权限
    name = models.CharField(max_length=20, null=False)
    url = models.CharField(max_length=20)
    menus = models.ForeignKey('Menu', blank=True, null=True)

    # competence = models.ForeignKey('Menu')
    def __str__(self):
        return self.name
