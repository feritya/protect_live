from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()
    created = models.DateField(auto_now_add=True)
    is_protect = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name+" - "+self.last_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + " - " + self.author.name 

class AuthorNotes(models.Model):
    title= models.CharField(max_length=100,blank=True,null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    note = models.TextField()
    


    def __str__(self):
        return self.title 
#sentry e sinyal gönderilecekk 

