from django.urls import path
from webapp.views import NumbersGetView

urlpatterns = []

numbers_url = [
    path('', NumbersGetView.as_view(), name='numbers')
]

urlpatterns += numbers_url
