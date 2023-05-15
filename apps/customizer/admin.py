from django.contrib import admin

from customizer.models import News, Project, Partner, Message, Tuzilma, Ilmiy


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('fio', 'subject', 'phone')


@admin.register(Ilmiy)
class IlmiyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


@admin.register(Tuzilma)
class TuzilmaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
