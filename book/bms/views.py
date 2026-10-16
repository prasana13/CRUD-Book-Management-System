
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


# Read: Display all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


# Create: Add a new book
def book_create(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            price=request.POST.get('price')
        )
        return redirect('book_list')

    return render(request, 'book_form.html', {'book': None})


# Update: Modify book details
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.save()
        return redirect('book_list')

    return render(request, 'book_form.html', {'book': book})


# Delete: Remove a book
def book_delete(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        book.delete()

    return redirect('book_list')
