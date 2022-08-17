from django.contrib import admin

from .models import Post, KeyWord

@admin.register(Post)
class AdminBase(admin.ModelAdmin):
    readonly_fields = ['created']

    list_display = [
        'id',
        'title',
        'subtitle',
        'type_post',
        'status',
        'updated',
    ]

    fields = [
        'title',
        'subtitle',
        'type_post',
        'status',
        'keyword',
        'content',
        'updated'
    ]


@admin.register(KeyWord)
class AdminKeyWords(admin.ModelAdmin):
    readonly_fields = ['created']

    list_display = [
        'id',
        'name',
    ]

    fields = [
        'name',
        'updated',
    ]