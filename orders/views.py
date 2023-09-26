from django.shortcuts import render
from django.views.generic import ListView
from .models import Order


class OrderList(ListView):
    model = Order
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset
    
