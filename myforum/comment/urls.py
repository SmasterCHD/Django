from django.conf.urls import url

urlpatterns = [
    url(r'^list/$', "comment.views.comment_list", name="comment_list"),
    url(r'^create/$', "comment.views.comment_create", name="comment_create"),
]