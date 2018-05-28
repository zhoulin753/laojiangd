from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Userinfo)
admin.site.register(Role)
admin.site.register(Menu)
admin.site.register(Competence)