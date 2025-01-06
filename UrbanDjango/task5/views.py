from django.shortcuts import render
from .forms import UserRegister

users = ['vasya1987', 'johnwick', 'optimus2005']


def sign_up(request):
    info = {'form_type': 'sign_up'}

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['success'] = f'Приветствуем, {username}!'
                form = UserRegister()
        else:
            info['error'] = 'Пожалуйста, исправьте ошибки в форме.'
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {'form_type': 'django_sign_up'}

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        repeat_password = request.POST.get('repeat_password', '').strip()

        try:
            age = int(request.POST.get('age', 0))
        except ValueError:
            age = 0

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            info['success'] = f'Приветствуем, {username}!'

    return render(request, 'fifth_task/registration_page.html', info)

