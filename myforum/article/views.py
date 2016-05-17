# coding:utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from models import Article
from block.models import Block
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

#C:\Python27\Lib\site-packages\django\contrib\auth\decorators.py
# Create your views here.
def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")
    return render_to_response("article_list.html", {"articles": articles,"blocks": block},
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


