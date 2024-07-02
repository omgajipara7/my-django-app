from django.urls import path
from . import views
from django.contrib import admin


urlpatterns=[
    path('admin/', admin.site.urls),
    path("0/",views.hello,name="hello"),
    path("1/",views.hellohtml,name="hellohtml"),
    path("2/",views.members,name="members"),
    path('2/details/<int:id>', views.details, name='details'),
    path("",views.main,name="main"),
    path("st/",views.student,name="student"),
    path("std/",views.stlist,name="stlist"),
    path('std/stdetails/<int:id>',views.stdetails,name="stdetails"),
    path('auth/',views.auth,name="auth"),
    path('login/',views.login,name="login"),
    path('login/stportal/<str:id>',views.stportal,name="stportal"),
    path('testing/',views.testing,name='testing'),
]