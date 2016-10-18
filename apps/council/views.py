# -*- encoding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import View, TemplateView, CreateView, ListView,\
    DetailView

from RWE.mixins import LoginRequiredMixin
from .models import Meeting, Point
import forms as council_forms


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'council/index.html'


class MeetingListView(LoginRequiredMixin, ListView):
    model = Meeting
    template_name = 'council/meeting_list.html'


class MeetingCreateView(LoginRequiredMixin, CreateView):
    form_class = council_forms.MeetingForm
    template_name = 'council/add_meeting.html'

    def get_success_url(self):
        return reverse_lazy('meeting_list')


class MeetingDetailView(LoginRequiredMixin, DetailView):
    model = Meeting
    template_name = 'council/meeting_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MeetingDetailView, self).get_context_data(**kwargs)
        context['point_list'] = Point.objects.filter(
            meeting__pk=self.object.pk)
        return context


class PointCreateView(LoginRequiredMixin, CreateView):
    form_class = council_forms.PointForm
    template_name = 'council/add_point.html'

    def form_valid(self, form):
        point = form.save(commit=False)
        meeting_pk = self.kwargs['pk']
        point.meeting = Meeting.objects.get(pk=meeting_pk)
        return super(PointCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('meeting_detail', args=(self.kwargs['pk'],))


class PointDetailView(LoginRequiredMixin, DetailView):
    model = Point
    template_name = 'council/point_detail.html'
