from data import BOOKS, CATEGORIES
from django.shortcuts import render

def index_view(request):
    context = {'books': BOOKS}
    return render(request, 'catalog/index.html', context)

def categories_view(request):
    context = {'categories': CATEGORIES}
    return render(request, template_name='catalog/categories.html', context=context)

def category_detail_view(request, name):
    public_books = []
    for book in BOOKS:
        if name in book['category']:
            public_books.append(book)
    return render(request, template_name='catalog/category.html', context={'books': public_books, 'category': name})

def book_detail_view(request, id):
    context = {}
    for book in BOOKS:
        if book['id'] == id:
            context = {'book': book}
            return render(request, template_name='catalog/book.html', context={'book':book})
    # Реализовать проверку на отсутсвие книги по id
    return render(request, template_name='catalog/index.html', context=context)