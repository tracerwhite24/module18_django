from django.shortcuts import render


def store_platform(request):
    return render(request, 'fourth_task/platform.html')


def store_goods(request):
    goods = {
        'Tabletops': ['BattleTech: Starter Set', 'Middle-earth Strategy Battle Game',
                      'Warhammer 40,000: Introductory Set']
    }
    return render(request, 'fourth_task/goods.html', context=goods)


def store_cart(request):
    return render(request, 'fourth_task/cart.html')
