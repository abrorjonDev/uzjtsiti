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
