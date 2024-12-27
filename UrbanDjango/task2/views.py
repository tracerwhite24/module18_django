from django.shortcuts import render
from django.views.generic import TemplateView


def cls_temp(request):
    return render(request, 'second_task/class_template.html')


def fnc_temp(request):
    return render(request, 'second_task/func_template.html')


class Classy(TemplateView):
    template_name = 'second_task/class_template.html'

