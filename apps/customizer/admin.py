from django.contrib import admin

from customizer.models import News
from customizer.forms import NewsForm


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

    # form_class = NewsForm
