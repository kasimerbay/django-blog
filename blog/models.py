from django.db import models


# Create your models here.

class Paper(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(default="Ahmet Kasım Erbay", max_length=25)
    title = models.CharField(max_length=60)
    date = models.DateField(auto_now=False, auto_now_add=False)
    post_link = models.URLField(default=None, max_length=200)

    def __str__(self):
        return f"{self.id} - {self.date} - {self.title}"

class Navs(models.Model):
    id = models.IntegerField(primary_key=True)
    nav_item = models.CharField(default=None, max_length=10)

    def __str__(self):
        return f"{self.id} - {self.nav_item}"

class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    link = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.id} - {self.name.capitalize()} account."
