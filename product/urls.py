from django.urls import path 
from .views import ProductList , ProductDetail , BrandList , BrandDetail , queryset_debug , add_review
from .api import  ProductListApi , ProductDetailApi ,BrandListApi , BrandDetailApi

app_name = 'product'


urlpatterns = [
    path('' , ProductList.as_view()),
    path('debug' ,queryset_debug),
    path('<slug:slug>' , ProductDetail.as_view()),
    path('<slug:slug>/add-review' , add_review,name='add-review'),

    path('brands/' , BrandList.as_view()),
    path('brands/<slug:slug>' , BrandDetail.as_view()),



    # api
    path('api/list' , ProductListApi.as_view()) ,
    path('api/list<int:pk>' , ProductDetailApi.as_view()) ,
    path('brands/api/list' , BrandListApi.as_view()) ,
    path('brands/api/list<int:pk>' , BrandDetailApi.as_view()) ,

]
