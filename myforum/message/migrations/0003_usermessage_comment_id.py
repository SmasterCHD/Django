# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20160528_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='comment_id',
            field=models.IntegerField(default=0, verbose_name='\u56de\u590d\u4fe1\u606fID'),
        ),
    ]
