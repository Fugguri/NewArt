from django.urls import path
from .views import *
from . import views
from django.http import request

urlpatterns = [
    path('', HomePaint.as_view(), name='gallery'),
    path('gallery', HomePaint.as_view(), name='gallery'),
    path('collection/<int:pk>/', PaintCollection.as_view(), name='collections'),
    path('years/<int:pk>/', PaintCollection.as_view(), name='years'),
    path('materials/<int:pk>/', PaintCollection.as_view(), name='materials'),
    path('orientation/<int:pk>/', PaintCollection.as_view(), name='orientation'),
    path('shop', ShopPaint.as_view(), name='shop'),
    path('paint/<int:pk>/', PaintView.as_view(), name='paint'),
    path('about', About.as_view(), name='about_me'),
    path('in_interior', In_Interior.as_view(), name='in_interior'),
    path('addbookmark/<int:pk>',
         views.addbokmarks, name='addbookmark'),
    path('bookmarks', BookmarksListView.as_view(), name="bookmarks")
]
