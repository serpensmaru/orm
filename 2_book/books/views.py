from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()

    numbers = len(books)
    if not (numbers % 2 == 0):
        numbers = (numbers + 1) // 2
    else:
        numbers = numbers // 2

    paginator = Paginator(books, numbers)
    current_page = int(request.GET.get('page', 1))
    page = paginator.get_page(current_page)
    context = {"books": page,
               "page": page
               }
    return render(request, template, context)

def book_date(request, pub_date):
    template = 'books/books_list.html'
    list_pub_date = [data.pub_date for data in Book.objects.all()]
    list_pub_date.sort()

    books = Book.objects.filter(pub_date=pub_date)


    paginator = Paginator(list_pub_date, 1)
    current_page = int(request.GET.get('page', 1))
    page = paginator.get_page(current_page)
    context = {"books": books,
               "data": page
               }


    return render(request, template, context)