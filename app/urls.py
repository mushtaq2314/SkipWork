from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('order',views.order,name='index'),
    path('login',views.login,name='login'),
    path('db',views.db,name='db'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)