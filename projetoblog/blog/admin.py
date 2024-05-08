from blog.models import Page, Post
from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 
    list_display_links = 'title',
    search_fields = 'id', 'title', 'content',
    list_per_page = 50
    ordering = '-id',

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title','created_by',
    list_display_links = 'title',
    search_fields = 'id', 'title', 'excerpt', 'content',
    list_per_page = 50
    ordering = '-id',
    readonly_fields = (
        'created_at', 'created_by',
        'link',
    )
    
    def link(self, obj):
        if not obj.pk:
            return '-'

        url_do_post = obj.get_absolute_url()
        safe_link = mark_safe(
            f'<a target="_blank" href="{url_do_post}">Ver post</a>'
        )

        return safe_link

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user  # type: ignore
        else:
            obj.created_by = request.user  # type: ignore

        obj.save()