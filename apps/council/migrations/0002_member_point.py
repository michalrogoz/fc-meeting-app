# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('council', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='Imi\u0119')),
                ('last_name', models.CharField(max_length=255, verbose_name='Nazwisko')),
                ('scientific_title', models.CharField(blank=True, max_length=1, null=True, verbose_name='Tytu\u0142/stopie\u0144 naukowy', choices=[(b'1', 'in\u017c.'), (b'2', 'mgr in\u017c.'), (b'3', 'dr'), (b'4', 'dr in\u017c.'), (b'5', 'dr hab.'), (b'6', 'dr hab. in\u017c.'), (b'7', 'prof. dr hab.'), (b'8', 'prof. dr hab. in\u017c.')])),
                ('in_small_quorum', models.BooleanField(default=False, verbose_name='Cz\u0142onek ma\u0142ego kworum')),
                ('lookup', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Adres e-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('point_type', models.CharField(max_length=255, verbose_name='Rodzaj sprawy')),
                ('title', models.CharField(max_length=255, verbose_name='Tytu\u0142')),
                ('description', models.TextField(verbose_name='Opis')),
                ('is_secret', models.BooleanField(default=False, verbose_name='Tajne g\u0142osowanie')),
                ('small_quorum', models.BooleanField(default=False, verbose_name='Ma\u0142e kworum')),
                ('owner', models.ForeignKey(verbose_name='Opiekun', to='council.Member')),
            ],
        ),
    ]
