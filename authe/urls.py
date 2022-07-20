from django.contrib import admin
from django.urls import path
from authe import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.base, name='base'),
    path('login', LoginView.as_view(template_name="login.html"), name='login'),
     path('register/', views.regist, name="regist"),
     path('center', views.center, name="center"),
     path('exit', LogoutView.as_view(next_page=views.base), name='exit'),
     path('export_item_xls/', views.export_xls), 
     path('export_itemsec_xls/', views.export_xls_section), 
]