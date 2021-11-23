from django.contrib import admin
from django.urls import path
from vehicledetail import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add/', views.add, name='add'),
    path('addfill/', views.addfill, name='addfill'),
    path('viewdetail/', views.viewdetail, name='viewdetail'),
    path('deletedata/<int:Sr>/', views.deletedata, name='deletedata'),
    path('<int:Sr>/', views.updatedata, name='updatedata'),
    path('handlesignup/', views.handlesignup, name='handlesignup'),
    path('handlelogin/', views.handlelogin, name='handlelogin'),
    path('handlelogout/', views.handlelogout, name='handlelogout'),
    path('<str:slug>/', views.furtherdetail, name='furtherdetail'),
]