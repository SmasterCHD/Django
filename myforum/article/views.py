# coding:utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from models import Article
from block.models import Block
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

#C:\Python27\Lib\site-packages\django\contrib\auth\decorators.py
# Create your views here.
def article_list(request,block_id):
    block_id = int(block_id)
    page_no = int(request.GET.get("page_no","1")) #page_no默认值为1
    block = Block.objects.get(id=block_id)
    articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")

    p = Paginator(articles, 10) #每页显示文章个数
    if page_no > p.num_pages:
        page_no = p.num_pages
    if page_no < 0:
        page_no = 1
    page_links = [i for i in range(page_no - 5, page_no + 6) if i > 0 and i <= p.num_pages]
    page = p.page(page_no)
    previous_link = page_links[0] - 1
    next_link = page_links[-1] + 1

    has_previous = previous_link > 0
    has_next = next_link <= p.num_pages

    return render_to_response("article_list.html",
                              {"articles": page.object_list,"blocks": block,
                               "has_previous":has_previous,"has_next":has_next,
                               "previous_link":previous_link,
                               "next_link":next_link,
                               "page_cnt":p.num_pages,
                               "current_no":page_no,
                               "page_links":page_links
                               },
                              context_instance=RequestContext(request)) #block不能当网页的参数名传回去
@login_required
def article_create(request,create_id):
    create_id = int(create_id)
    block = Block.objects.get(id=create_id)
    if request.method == "GET":
        return render_to_response("article_create.html", {"blocks": block},
                              context_instance=RequestContext(request))
    else: #request.method == "POST"
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not  content:
            messages.add_message(request,messages.ERROR,u"标题和内容均不能为空")
            return render_to_response("article_create.html", {"blocks": block, "title": title, "content": content},
                              context_instance=RequestContext(request))
        owner = User.objects.all()[0]
        new_article = Article(block=block,owner=request.user,title=title,content=content)
        new_article.save()
        messages.add_message(request,messages.INFO,u"成功发布文章")
        return redirect(reverse("article_list",args=[block.id]))




def article_detail(request,art_id):
    art_id = int(art_id)
    art = Article.objects.get(id=art_id)
    return render_to_response("article_detail.html", {"art": art},
                              context_instance=RequestContext(request))


