from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.root,name = "root"),
    path('<str:type>',views.fun1,name="details")
    #path('admin/', admin.site.urls),
]