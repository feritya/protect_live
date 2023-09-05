from django.urls import path
from . import views

urlpatterns = [
    # Diğer url pattern'ları...
    # path('delete_author/<int:author_id>/', views.delete_author, name='delete_author'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('', views.AuthorListView.as_view(), name='author_list'),
    path('book_list/', views.book_list, name='book_list'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('note_list/', views.note_list, name='note_list'),
    path('object_list/<int:author_id>/', views.object_list, name='object_list'),
    path('delete_non_protected_author/<int:author_id>/', views.delete_non_protected_author, name='delete_non_protected_author'),
    path('detail_book/<int:book_id>/', views.detail_book, name='detail_book'),
    path('detail_note/<int:note_id>/', views.detail_note, name='detail_note'),
]
