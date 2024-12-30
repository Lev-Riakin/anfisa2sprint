from django.shortcuts import render

from ice_cream.models import IceCream

from django.db.models import Q


def index(request):
    template_name = 'homepage/index.html'
    # Заключаем вызов методов в скобки
    # (это стандартный способ переноса длинных строк в Python);
    # каждый вызов пишем с новой строки, так проще читать код:
    ice_cream_list = IceCream.objects.values(
            'id', 'title', 'description'
        # Верни только те объекты, у которых в поле is_on_main указано True:
        ).filter(Q(is_published=True) & (Q(is_on_main=True) | Q(title__contains='пломбир')))
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)
