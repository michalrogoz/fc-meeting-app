# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('council', '0003_remove_meeting_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateTimeField(verbose_name='Data spotkania'),
        ),
    ]
