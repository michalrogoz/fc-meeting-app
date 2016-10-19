# -*- encoding: utf-8 -*-

from datetime import datetime

from django import forms
from bootstrap3_datetime.widget import DateTimePicker

from functools import partial

from .models import Meeting, Point


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        widgets = {
            'date': DateTimePicker(options={'id': 'date_picker',
                                            "format": "DD-MM-YYYY HH:mm",
                                            'sideBySide': True}),
        }

        exclude = ['code',]

    def clean(self):
        cd = self.cleaned_data

        print cd
        print self.errors
        if self.data['date']:
            cd['date'] = datetime.strptime(self.data['date'], '%d-%m-%Y %H:%M')
            print datetime.strptime(self.data['date'], '%d-%m-%Y %H:%M'), type(
                datetime.strptime(self.data['date'], '%d-%m-%Y %H:%M'))
            del self.errors['date']
        else:
            self.errors['date'] = u'Pole nie może być puste'

        return cd


class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        exclude = ('meeting',)
