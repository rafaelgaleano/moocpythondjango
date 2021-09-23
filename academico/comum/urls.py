# -*- coding: utf-8 -*-
from django.urls import path, re_path
from academico.comum import views

urlpatterns = [
    re_path(path('', views.home, name='home')),
    re_path(r'^admin/', include('admin.site.urls', 'admin'), namespace='admin'),

]
# path('comum/', views.home)