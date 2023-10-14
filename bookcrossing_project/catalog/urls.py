from django.urls import path

from . import views
urlpatterns = [
    path('', views.index_view),
    path('categories/', views.categories_view),
    path('categories/<int:id>/', views.category_detail_view),
    path('book/<int:id>/', views.book_detail_view),
]
