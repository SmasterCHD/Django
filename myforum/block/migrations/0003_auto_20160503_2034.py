# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20160430_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='manager',
            field=models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL),
        ),
    ]
