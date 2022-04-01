from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView


class NumbersGetView(TemplateView):
    template_name = 'numbers.html'



