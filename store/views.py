from django.shortcuts import render
from django.http import JsonResponse
from .models import DATABASE

def product_view(request):
    if request.method == 'GET':
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})

# Create your views here.
