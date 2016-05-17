# coding:utf-8
from django.contrib.auth.models import User
from django.db import models

class Block(models.Model):
    name = models.CharField(u'名字', max_length=38)
    desc = models.CharField(u'描述', max_length=38)
    # sex = models.IntegerField(u'性别', choices=((1, u'男'), (2, u'女')))
    manager = models.ForeignKey(User, verbose_name=u'作者')

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'模板'  #好像是主目录和子目录的区别
        verbose_name_plural = u'模板'


# Create your models here.
