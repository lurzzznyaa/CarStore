from django.urls import path
from . import views
from .views import index_view, one_item, one_category, add_car

urlpatterns = [
    path('', index_view, name='main'),
    path('car/<int:pk>', one_item, name='car'),
    path('category/<str:category>', one_category, name='category'),
    path('add/', add_car, name='add_car'),
]
