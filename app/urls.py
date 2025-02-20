from django.urls import path
from . import views
from .views import index_view, one_item, one_category, add_car, add_car_2, car_delete, one_item_2

urlpatterns = [
    path('', index_view, name='main'),
    path('car/<int:pk>', one_item, name='car'),
    path('car_2/<int:pk>/', one_item_2, name='car_2'),
    path('category/<str:category>', one_category, name='category'),
    path('add/', add_car, name='add_car'),
    path('add_2/', add_car_2, name='add_car_2'),
    path('delete/<int:pk>/', car_delete, name='delete')
]
