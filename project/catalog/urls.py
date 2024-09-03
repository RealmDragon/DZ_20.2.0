from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),  # Главная страница - список продуктов
    path('categories/<slug:slug>/', views.ProductListView.as_view(), name='product_list_by_category'),  # Фильтрация по категории
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),  # Детали продукта
    path('categories/', views.CategoryListView.as_view(), name='category_list'),  # Список категорий
    path('home/', views.home, name='home'),  #  Добавьте эту строку
    path('contact/', views.contact, name='contact'),  #  Добавьте эту строку
    path('index/', views.index, name='index'),  #  Добавьте эту строку
]

