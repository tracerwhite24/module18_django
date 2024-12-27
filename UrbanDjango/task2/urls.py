from django.urls import path
from . import views

urlpatterns = [
    path('class', views.cls_temp, name='class'),
    path('func/', views.fnc_temp, name='func'),
]

