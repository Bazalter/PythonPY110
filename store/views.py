from django.shortcuts import render
from django.http import JsonResponse
from .models import DATABASE
from django.http import HttpResponse, HttpResponseNotFound
from logic.services import filtering_category

def products_view(request):
    if request.method == 'GET':
        if id_ := request.GET.get('id'):
            if DATABASE.get(id_):
                return JsonResponse(DATABASE[id_], json_dumps_params={'ensure_ascii': False,
                                                 'indent': 4})
            return HttpResponseNotFound("Данного продукта нет в базе данных")

            # Обработка фильтрации из параметров запроса
        category_key = request.GET.get("category")  # Считали 'category'
        if ordering_key := request.GET.get("ordering"):  # Если в параметрах есть 'ordering'
            if request.GET.get("reverse") in ('true', 'True'):  # Если в параметрах есть 'ordering' и 'reverse'=True
                data = filtering_category(DATABASE, category_key, ordering_key, True)  # TODO Провести фильтрацию с параметрами
            else:
                data = filtering_category(DATABASE, category_key, ordering_key)  # TODO Провести фильтрацию с параметрами
        else:
            data = filtering_category(DATABASE, category_key)  # TODO Провести фильтрацию с параметрами
        # В этот раз добавляем параметр safe=False, для корректного отображения списка в JSON
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False,
                                                                 'indent': 4})

def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()
            return HttpResponse(data)


def products_page_view(request, page):
    if request.method == "GET":
        if isinstance(page, str):
            for data in DATABASE.values():
                if data['html'] == page:  # Если значение переданного параметра совпадает именем html файла
                    with open(f'store/products/{page}.html', encoding='utf-8') as f:
                        return HttpResponse(f.read())
        elif isinstance(page, int):
            data = DATABASE.get(str(page))  # Получаем какой странице соответствует данный id
            if data:  # Если по данному page было найдено значение
                with open(f'store/products/{data["html"]}.html', encoding='utf-8') as f:
                    return HttpResponse(f.read())


        # Если за всё время поиска не было совпадений, то значит по данному имени нет соответствующей
        # страницы товара и можно вернуть ответ с ошибкой HttpResponse(status=404)
        return HttpResponse(status=404)


# Create your views here.
