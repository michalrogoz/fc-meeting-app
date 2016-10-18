# -*- encoding: utf-8 -*-
from django.db import models

TITLES_CHOICES = [
    ('1', u'inż.'),
    ('2', u'mgr inż.'),
    ('3', u'dr'),
    ('4', u'dr inż.'),
    ('5', u'dr hab.'),
    ('6', u'dr hab. inż.'),
    ('7', u'prof. dr hab.'),
    ('8', u'prof. dr hab. inż.'),
]


class Meeting(models.Model):
    date = models.DateTimeField(
        verbose_name=u'Data spotkania')
    code = models.CharField(blank=True, null=True, max_length=255)

    def save(self, *args, **kwargs):
        self.code = u'{}/{}'.format(self.date.isocalendar()[0],
                                    self.date.isocalendar()[1])
        super(Meeting, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'Rada Wydziału Elektroniki {}'.format(self.code)


class Point(models.Model):
    meeting = models.ForeignKey(
        'Meeting',
        verbose_name=u'Spotkanie')
    owner = models.ForeignKey(
        'Member',
        verbose_name=u'Opiekun')
    point_type = models.CharField(
        max_length=255,
        verbose_name=u'Rodzaj sprawy')
    title = models.CharField(
        max_length=255,
        verbose_name=u'Tytuł')
    description = models.TextField(
        verbose_name=u'Opis')
    is_secret = models.BooleanField(
        default=False,
        verbose_name=u'Tajne głosowanie')
    small_quorum = models.BooleanField(
        default=False,
        verbose_name=u'Małe kworum')


class Member(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name=u'Imię')
    last_name = models.CharField(
        max_length=255,
        verbose_name=u'Nazwisko')
    scientific_title = models.CharField(
        max_length=1, blank=True, null=True,
        choices=TITLES_CHOICES,
        verbose_name=u'Tytuł/stopień naukowy')
    in_small_quorum = models.BooleanField(
        default=False,
        verbose_name=u'Członek małego kworum')
    lookup = models.CharField(
        blank=True, null=True,
        max_length=255)
    email = models.EmailField(
        verbose_name=u'Adres e-mail')

    def save(self, *args, **kwargs):
        if self.scientific_title:
            self.lookup = u'{} {} {}'.format(
                TITLES_CHOICES[int(self.scientific_title)-1][1],
                self.first_name,
                self.last_name)
            if int(self.scientific_title) >= 5:
                self.in_small_quorum = True
        else:
            self.lookup = u'{} {}'.format(self.first_name, self.last_name)
        super(Member, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'{}'.format(self.lookup)
