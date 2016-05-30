from django.contrib import admin
from models import  Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id","block", "article","content", "owner","to_comment_id", "create_timestamp", "last_update_timestamp")
    search_fields = ("content",)
    list_filter = ("block",)

admin.site.register(Comment, CommentAdmin)