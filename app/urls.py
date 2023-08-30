from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('order',views.order,name='intermediate'),
    path('intermediate',views.intermediate,name='index'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('delete_order/<str:order_id>/',views.delete_order,name='deleteOrder'),
    path('db',views.db,name='db'),
    path('contact',views.contact,name='contact'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)