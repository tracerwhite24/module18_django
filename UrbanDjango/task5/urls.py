from django.urls import path
from .views import sign_up, sign_up_by_html

urlpatterns = [
    path('', sign_up, name='sign_up'),
    path('django_sign_up', sign_up_by_html, name='sign_up_by_html'),
]
