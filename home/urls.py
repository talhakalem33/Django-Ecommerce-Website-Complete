from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('productlist/<str:category_slug>/', views.productlist, name='productlist'),
    path('contact', views.contact, name="contact"),
    path('aboutus', views.aboutUs, name='aboutUs'),
    path('product/<slug:slug>', views.product, name='product'),
    path('cart', views.cart, name='cart'),
    path('campaignproductlist/<str:campaign_slug>/', views.campaignproductlist, name='campaignproductlist'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
