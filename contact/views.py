from django.shortcuts import render

from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import data
from django.views.generic.edit import CreateView

# Create your views here.

class homeView(ListView):
    model = data
    template_name = "home.html"
    context_object_name = 'datas'

class newView(CreateView):
    model = data
    template_name = 'create.html'
    fields = ('__all__')
    success_url = reverse_lazy('home')

class detailView(DetailView):
    model = data
    template_name = 'detail.html'
    fields = ('__all__')
    context_object_name = 'info'


class portfolioView(TemplateView):
    template_name = 'portfolio.html'