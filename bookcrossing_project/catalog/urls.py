from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('categories/', views.categories_view, name='categories_view'),
    path('categories/<int:id>/', views.category_detail_view, name='category_detail_view'),
    path('book/<int:id>/', views.book_detail_view, name='book_detail_view'),
]
