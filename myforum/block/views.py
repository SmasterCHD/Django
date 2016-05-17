# coding:utf-8
from django.shortcuts import render_to_response
from models import Block
from django.template import RequestContext


# Create your views here.
def block_list(request):
    blocks = Block.objects.all().order_by("id") #id 带 - 号为倒序
    return render_to_response("block_list.html", {"blocks": blocks},
                              context_instance=RequestContext(request))
