from django.urls import path
from .views import cls_temp, fnc_temp

urlpatterns = [
    path('', cls_temp, name='class'),
    path('func', fnc_temp, name='func'),
]
