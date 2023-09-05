from django.contrib import admin
from .models import  Author,Book,AuthorNotes


# Register your models here.


# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'last_name', 'created')
#     list_filter = ('name', 'last_name')
    
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(AuthorNotes)