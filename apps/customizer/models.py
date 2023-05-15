from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.CharField(max_length=300)
    short_description = models.CharField(max_length=600)
    article = RichTextField()
    image = models.ImageField(upload_to="images/n/", null=True)
    slug = models.SlugField(max_length=255, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def __str__(self):
        return self.title

#
# class Employee(models.Model):
#     full_name = models.CharField(max_length=255)


class Project(models.Model):
    image = models.ImageField(upload_to='images/p/')
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    data_delay = models.PositiveIntegerField(default=200)

    def __str__(self):
        return self.title


class Partner(models.Model):
    image = models.ImageField(upload_to='images/partners/')


class Message(models.Model):
    fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=18)
    subject = models.CharField(max_length=155)
    message = models.CharField(max_length=2000)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.fio


class Tuzilma(models.Model):
    TYPES = (
        ('director', 'Direktor'),
        ('ilmiy-kengash', 'Ilmiy kengash'),
        ('institut-kengashi', 'Institut kengashi'),
    )
    title = models.CharField(max_length=50)
    page = RichTextField()
    slug = models.CharField(max_length=50, choices=TYPES, default='')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Tuzilma"


class Ilmiy(models.Model):
    TYPES = (
        ('labs', 'Laboratoriyalar'),
        ('projects', 'Loyihalar'),
        ('ilmiy-uslubiy-ishlar', 'Ilmiy uslubiy ishlar'),
    )
    slug = models.CharField(max_length=50, choices=TYPES, default='labs')
    title = models.CharField(max_length=50)
    page = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ilmiy"