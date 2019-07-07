from django.db import models

# Create your models here.

class Books(models.Model):
    bname = models.CharField(max_length=255, blank=True, null=True)
    book_id = models.CharField(max_length=255, blank=False, null=False, primary_key=True)
    no_copies = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'books_easy'


class User(models.Model):
    uname = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=False, null=False, primary_key=True)

    class Meta:
        managed = True
        db_table = 'user'