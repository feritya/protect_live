from django.shortcuts import render,get_object_or_404,redirect
from django.db.models.deletion import ProtectedError
from .models import Author, Book,AuthorNotes
from django.contrib.admin.utils import get_deleted_objects
from django.db.models import ProtectedError
from django.views import View
import sentry_sdk




class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        protected_books=[]
        protected_notes=[]

        for author in authors:
            books=[]
            notes=[]
            protected_books += Book.objects.filter(author=author)
            protected_notes += AuthorNotes.objects.filter(author=author) 
            print(protected_books)
            print(protected_notes)
            books=Book.objects.filter(author=author)
            notes=AuthorNotes.objects.filter(author=author) 

            author.is_protect=False
            author.save()
            if books or notes:
                author.is_protect=True
                author.save()
        return render(request, 'author_list.html', {'authors': authors,"protected_notes":protected_notes,"protected_books":protected_books})
        
    
    def post(self, request):
        authors = Author.objects.all()
        protected_books=[]
        protected_notes=[]

        for author in authors:
            try:
                author.delete()
            except ProtectedError:
                sentry_sdk.capture_exception(ProtectedError)
                protected_books = Book.objects.filter(author=author)
                protected_notes = AuthorNotes.objects.filter(author=author)
        return render(request, 'author_list.html', {'authors': authors,'protected_books':protected_books,'protected_notes':protected_notes})
         
def delete_non_protected_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
        
    return render(request, 'author_list.html', {'author': author})

def object_list(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author=author)
    notes = AuthorNotes.objects.filter(author=author)
    return render(request, 'object_list.html', {'author': author,'books':books,'notes':notes})

def detail_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    return render(request, 'detail_book.html', {'book': book})

def detail_note (request, note_id):
    note = get_object_or_404(AuthorNotes, pk=note_id)

    return render(request, 'detail_note.html', {'note': note})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('author_list') 
        
    return render(request, 'note_list.html', {'book': book})

def delete_note(request, note_id):
    note = get_object_or_404(AuthorNotes, pk=note_id)
    
    if request.method == 'POST':
        note.delete()
        return redirect('author_list')
        
    return render(request, 'book_list.html', {'note': note})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def note_list(request):
    notes = AuthorNotes.objects.all()
    return render(request, 'note_list.html', {'notes': notes})