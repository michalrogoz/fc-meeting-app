from django.views.generic import TemplateView

from RWE.mixins import LoginRequiredMixin


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
