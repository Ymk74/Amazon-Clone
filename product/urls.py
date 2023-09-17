from django.urls import path 
from .views import ProductList , ProductDetail , BrandList , BrandDetail , queryset_debug
from .api import  ProductListApi , ProductDetailApi ,BrandListApi , BrandDetailApi

urlpatterns = [
    path('' , ProductList.as_view()),
    path('debug' ,queryset_debug),
    path('<slug:slug>' , ProductDetail.as_view()),
    path('brands/' , BrandList.as_view()),
    path('brands/<slug:slug>' , BrandDetail.as_view()),



    # api
    path('api/list' , ProductListApi.as_view()) ,
    path('api/list<int:pk>' , ProductDetailApi.as_view()) ,
    path('brands/api/list' , BrandListApi.as_view()) ,
    path('brands/api/list<int:pk>' , BrandDetailApi.as_view()) ,

]
