# coding:utf-8
from django.contrib import admin
from models import  Article
from comment.models import Comment
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    fieldsets = (
        (None, {
            'fields': ('owner', 'to_comment_id', 'content')
        }),
    )

CommentInline.can_delete = False
CommentInline.max_num = 5
CommentInline.min_num = 0

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "block", "owner","status", "create_timestamp", "last_update_timestamp")
    search_fields = ("title", "content")
    list_filter = ("block", )

    inlines = [CommentInline]



    fieldsets = (
        (None, {
            'fields': ('block', 'title', 'owner', 'content',"status")
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            "fields": ("block","create_timestamp")
        }),
    )




    readonly_fields = ("block","title","owner", "content", "status", "create_timestamp")

    actions = ["make_picked"]
    def make_picked(modeladmin, request, queryset):
        for a in queryset:
            a.status = 10
            a.save()
    make_picked.short_description = u"设置精华"




admin.site.register(Article, ArticleAdmin)
