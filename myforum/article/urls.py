from django.conf.urls import url


urlpatterns = [
    url(r'^lists/(?P<block_id>\d+)', "article.views.article_list", name="article_list"),
    url(r'^detail/(?P<art_id>\d+)', "article.views.article_detail", name="article_detail"),
    url(r'^create/(?P<create_id>\d+)', "article.views.article_create", name="article_create"),
]
