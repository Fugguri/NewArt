from django.shortcuts import render, get_object_or_404, get_list_or_404,redirect
from .models import Paint, Collection, Year, Material, Orientation
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator


class HomePaint(ListView):
    paginate_by = 21
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
        


    
    
class PaintView(DetailView):
    model = Paint
    template_name = 'paints/details.html'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url


class ShopPaint(ListView):
    model = Paint
    template_name = 'paints/shop.html'
    context_object_name = 'paints'
    # extra_context = {'title': 'Главная'}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Магазин'
        return context

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        
    # def get_queryset(self):
    #     return Paint.objects.filter(is_published=True)


class About(ListView):
    model = Paint
    template_name = 'paints/about_me.html'
    context_object_name = 'paints'
    extra_context = {'title': 'Обо мне'}


class PaintCollection(ListView):
    model = Paint
    template_name = 'paints/gallery.html'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def get_queryset(self):
        return Paint.objects.filter(collection_id=self.kwargs['pk'])