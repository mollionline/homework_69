import json

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from api_app.validators import is_digit


@csrf_exempt
def add_numbers_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            answer = json.loads(request.body)
            if is_digit(str(answer['A'])) and is_digit(str(answer['B'])):
                answer = float(answer['A']) + float(answer['B'])
                return JsonResponse({'answer': answer}, safe=False)
            response = JsonResponse({'error': 'Value error'}, safe=False)
            response.status_code = 400
            return response
        else:
            response = JsonResponse({'error': 'You forgot to enter numbers to add'}, safe=False)
            response.status_code = 400
            return response


@csrf_exempt
def subtract_numbers_view(request, *args, **kwargs):
    if request.method == 'POST':
        answer = json.loads(request.body)
        if is_digit(str(answer['A'])) and is_digit(str(answer['B'])):
            answer = float(answer['A']) - float(answer['B'])
            return JsonResponse({'answer': answer}, safe=False)
        response = JsonResponse({'error': 'Value error'}, safe=False)
        response.status_code = 400
        return response
    else:
        response = JsonResponse({'error': 'You forgot to enter numbers to add'}, safe=False)
        response.status_code = 400
        return response


@csrf_exempt
def multiply_numbers_view(request, *args, **kwargs):
    if request.method == 'POST':
        answer = json.loads(request.body)
        if is_digit(str(answer['A'])) and is_digit(str(answer['B'])):
            answer = float(answer['A']) * float(answer['B'])
            return JsonResponse({'answer': answer}, safe=False)
        response = JsonResponse({'error': 'Value error'}, safe=False)
        response.status_code = 400
        return response
    else:
        response = JsonResponse({'error': 'You forgot to enter numbers to add'}, safe=False)
        response.status_code = 400
        return response


@csrf_exempt
def divide_numbers_view(request, *args, **kwargs):
    if request.method == 'POST':
        answer = json.loads(request.body)
        if is_digit(str(answer['A'])) and is_digit(str(answer['B'])):
            if float(answer['B']) != 0:
                answer = float(answer['A']) / float(answer['B'])
                return JsonResponse({'answer': answer}, safe=False)
            response = JsonResponse({'error': 'Division by zero'}, safe=False)
            response.status_code = 400
            return response
        response = JsonResponse({'error': 'Value error'}, safe=False)
        response.status_code = 400
        return response
    else:
        response = JsonResponse({'error': 'You forgot to enter numbers to add'}, safe=False)
        response.status_code = 400
        return response


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')
