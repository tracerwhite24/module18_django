from django.shortcuts import render


def cls_temp(request):
    context = {
        'title': 'Class Template',
        'message': 'Приветствую в шаблоне для классового представления',
    }
    return render(request, 'task2/class_template.html', context)


def fnc_temp(request):
    context = {
        'title': 'Func Template',
        'message': 'Приветствую в шаблоне для функционального представления',
    }
    return render(request, 'task2/func_template.html', context)



