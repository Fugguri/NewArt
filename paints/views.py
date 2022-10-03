from django.shortcuts import render, get_object_or_404, get_list_or_404,redirect

from .models import Paint
from django.views.generic import ListView, DetailView, CreateView


class HomePaint(ListView):
    model = Paint
    template_name = 'paints/gallery.html'
    context_object_name = 'paints'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        
    # def get_queryset(self):
    #     return Paint.objects.filter(is_published=True)
    
    
class PaintView(ListView):
    model = Paint
    template_name = 'paints/details.html'
    context_object_name = 'paint'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    # def get_queryset(self):
    #     return Paint.objects.filter(is_published=True)
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

class ShopPaint(ListView):
    model = Paint
    template_name = 'paints/shop.html'
    context_object_name = 'paints'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        
    # def get_queryset(self):
    #     return Paint.objects.filter(is_published=True