from django.shortcuts import render
from django.views.generic import ListView
from .models import Order ,Cart , CartDetail,OrderDetail , Coupon


class OrderList(ListView):
    model = Order
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset
    



def checkout(request):
    cart = Cart.objects.get(user=request.user,status='InProgress')
    cart_detail = CartDetail.objects.filter(cart=cart)


    return render(request ,'orders\checkout.html',{'cart_detail':cart_detail})
