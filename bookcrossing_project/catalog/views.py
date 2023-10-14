from django.shortcuts import render

def index_view(request):
    return render(request, template_name='catalog/index.html')

def categories_view(request):
    return render(request, template_name='catalog/categories.html')

def category_detail_view(request, id):
    return render(request, template_name='catalog/category.html')

def book_detail_view(request, id):
    return render(request, template_name='catalog/book.html')