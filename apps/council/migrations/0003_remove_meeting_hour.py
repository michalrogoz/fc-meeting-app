# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('council', '0002_member_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='hour',
        ),
    ]
