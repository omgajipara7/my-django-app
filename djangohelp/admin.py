# djangohelp/admin.py

from django.contrib import admin
from .models import Student,Auth,Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname','phone', 'joined_date')

admin.site.register(Member, MemberAdmin)



class AuthAdmin(admin.ModelAdmin):
    list_display=('username','password','enroll','branch')

admin.site.register(Auth,AuthAdmin)




admin.site.register(Student)




