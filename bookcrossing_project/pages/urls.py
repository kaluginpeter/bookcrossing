from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.about_view, name='about_views'),
]