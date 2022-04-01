from core.urls import path

from api_app.views import (get_token_view,
                           add_numbers_view,
                           subtract_numbers_view,
                           multiply_numbers_view,
                           divide_numbers_view)

urlpatterns = [
    path('csrf', get_token_view),
    path('add/', add_numbers_view),
    path('subtract/', subtract_numbers_view),
    path('multiply/', multiply_numbers_view),
    path('divide/', divide_numbers_view)
]
