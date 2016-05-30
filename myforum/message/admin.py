from django.contrib import admin
from models import  UserMessage
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ("owner", "content", "link", "comment_id","status","create_timestamp", "last_update_timestamp")
    search_fields = ("link", "content")
    list_filter = ("owner", )


admin.site.register(UserMessage, MessageAdmin)

# Register your models here.
