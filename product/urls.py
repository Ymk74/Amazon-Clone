from django.urls import path 
from .views import ProductList , ProductDetail , BrandList


urlpatterns = [
    path('' , ProductList.as_view()),
    path('<int:pk>' , ProductDetail.as_view()),
    path('brands' , BrandList.as_view())
]
