from django.shortcuts import redirect
from .models import Paint, Collection, Year, Material, Orientation, BookmarksModel
from django.views.generic import ListView, DetailView, CreateView, View
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect


class HomePaint(ListView):
    paginate_by = 21
    model = Paint
    template_name = 'paints/gallery.html'
    context_object_name = 'paints'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['collections'] = Collection.objects.all()
        context['years'] = Year.objects.all()
        context['materials'] = Material.objects.all()
        context['orientation'] = Orientation.objects.all()
        return context

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url


class PaintCollection(HomePaint):
    model = Paint
    template_name = 'paints/gallery.html'
    context_object_name = 'paints'
    allow_empty: bool = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Collection.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Paint.objects.filter(collection_id=self.kwargs['pk'])


class PaintView(DetailView):
    model = Paint
    template_name = 'paints/details.html'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url


class ShopPaint(HomePaint):

    template_name = 'paints/shop.html'
    context_object_name = 'paints'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Магазин'
        return context


class About(HomePaint):

    template_name = 'paints/about_me.html'
    context_object_name = 'paints'
    extra_context = {'title': 'Обо мне'}


class In_Interior(HomePaint):

    template_name = 'paints/in_interior.html'
    context_object_name = 'paints'
    extra_context = {'title': 'В интерьере'}


class Addbookmark(View):
    def post(self, request, pk):
        paint = Paint.objects.get(id=pk)
        new_bookmark = BookmarksModel.objects.create(paint=paint)
        session_bookmarks = request.session.get("bookmarks_id", [])
        session_bookmarks.append(new_bookmark.id)
        request.session['bookmarks_id'] = session_bookmarks
        return redirect('/bookmarks')


class BookmarksListView(ListView):
    model = BookmarksModel
    context_object_name = 'bookmarks'
    template_name = 'bookmarks/bookmarks.html'

    def get_queryset(self):
        return self.model.objects.filter(id__in=self.request.session.get("bookmarks_id", []))
