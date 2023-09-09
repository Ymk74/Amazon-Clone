from django.urls import path 
from .views import ProductList , ProductDetail , BrandList , BrandDetail , queryset_debug


urlpatterns = [
    path('' , ProductList.as_view()),
    path('debug' ,queryset_debug),
    path('<slug:slug>' , ProductDetail.as_view()),
    path('brands' , BrandList.as_view()),
    path('brands/<slug:slug>' , BrandDetail.as_view()),
]
