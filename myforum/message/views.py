# coding:utf-8
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import UserMessage
from comment.models import Comment
from utils.macro import COM_CNT_PER_PAGE

# Create your views here.
@login_required
def message_list(request):
    read_messages = UserMessage.objects.filter(owner=request.user,status=1).order_by("-id")
    unread_messages = UserMessage.objects.filter(owner=request.user,status=0).order_by("-id")
    return render_to_response("message_list.html", {"read_messages": read_messages,"unread_messages": unread_messages},
                              context_instance=RequestContext(request))

@login_required
def message_read(request, message_id):
    message = UserMessage.objects.get(id=int(message_id))


    comments = Comment.objects.get(id=message.comment_id)
    comments2 = Comment.objects.filter(article=comments.article)
    ids = list(comments2.values_list("id",flat=True))
    flg = ids.index(comments.id)
    coment_page = int((flg+COM_CNT_PER_PAGE)/COM_CNT_PER_PAGE)

    message.status = 1
    message.save()
    message_Link = message.link + "?comment_page_no=" +str(coment_page)+"#comment_id"+str(message.comment_id)

    return redirect(message_Link)