from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics


@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()[:20]  # list
    data = ProductSerializer(products,many=True,context={'request':request}).data  # json
    return Response({'products':data})



@api_view(['GET'])
def product_detail_api(request,product_id):
    products = Product.objects.get(id=product_id)  # list
    data = ProductSerializer(products,context={'request':request}).data  # json
    return Response({'product':data})


class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer