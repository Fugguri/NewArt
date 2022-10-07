from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', HomePaint.as_view(), name='index'),
    path('gallery', HomePaint.as_view(), name='gallery'),
    path('gallery/<int:pk>', PaintCollection.as_view(), name='gallery'),
    path('shop', ShopPaint.as_view(), name='shop'),
    path('paint/<int:pk>/', PaintView.as_view(), name='paint'),
    path('about', About.as_view(), name='about_me')
]