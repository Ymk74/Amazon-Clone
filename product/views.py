from django.shortcuts import render , redirect
from django.views.generic import ListView , DetailView
from .models import Product ,Brand ,ProductImages ,Review
from django.db.models import Q , F , Value
from django.db.models.aggregates import Max , Min , Count , Avg , Sum
from django.views.decorators.cache import cache_page

from .tasks import send_emails

from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.


# @cache_page(60 * 1)
def queryset_debug(request):
    #data = Product.objects.select_related('brand').all()  # prefetch_related = many-to-many
    #data = Product.objects.filter(price__gt=70)
    #data = Product.objects.filter(price__gte=70)
    #data = Product.objects.filter(price__lt=70)
    #data = Product.objects.filter(price__lt=70)
    #data = Product.objects.filter(price__range= (65,70))

    # navigate_relation
    #data = Product.objects.filter(brand__name='Apple')
    #data = Product.objects.filter(brand__price__gt=20)

    # filter with text
    #data = Product.objects.filter(name__contains='Brown')
    #data = Product.objects.filter(name__startswith='Grac')
    #data = Product.objects.filter(name__endswith='Brown')
    #data = Product.objects.filter(tags__isnull=True)


    # filter with date time
    #data = Review.objects.filter(created_at__year=2023)
    #data = Review.objects.filter(created_at__month=2023)

    #filter 2 values
    #data = Product.objects.filter(price__gt=80 , quantity__lt=10) # and
    #data = Product.objects.filter(
    #    Q(price__gt=80) |
    #    Q(price__gt=80 )
    #    ) # or

    #    data = Product.objects.filter(
    #    Q(price__gt=80) &
    #    Q(price__gt=80 )
    #    ) # and

    #data = Product.objects.filter(
    #    Q(price__gt=80) &
    #    ~Q(price__gt=80 )
    #    ) # and with not

    #عشان اقارن عمود بعمود
    #data = Product.objects.filter(price=F('quantity'))

    # ordering
    #data = Product.objects.all().order_by('name')   #Asc
    #data = Product.objects.order_by('name')         #Asc
    #data = Product.objects.order_by('-name')        # Dec
    #data = Product.objects.order_by('name').reverse()         # Dec
    #data = Product.objects.order_by('name','-quantity')    
    #data = Product.objects.order_by('name','quantity')  


    #data = Product.objects.order_by('name')[0]   # first     
    #data = Product.objects.order_by('name','quantity')[-1]    # last 

    #data = Product.objects.earliest('name')   # first     
    #data = Product.objects.latest('name','quantity')   # last 

    # slice
    #data = Product.objects.all()[:10]

    # select columns
    #data = Product.objects.values('name','price')
    #data = Product.objects.values('name','price','brand_name')
    #data = Product.objects.values_list('name','price','brand__name')

    # remove duplicate
    #data = Product.objects.all().distinct()

    # 
    #data = Product.objects.only('name' , 'price')
    #data = Product.objects.defer('slug','description')

    # aggregation 
    #data = Product.objects.aggregate(Sum('quantity'))
    #data = Product.objects.aggregate(Avg('price'))

    
    # annotate 
    # data = Product.objects.annotate(price_with_tax=F('price')*1.2)

    data = Product.objects.all()

    send_emails.delay()

    return render(request , 'product\debug.html',{'data':data})




class ProductList(ListView):
    model = Product
    paginate_by = 30


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["related_products"] = Product.objects.filter(brand=self.get_object().brand)
        return context
    


class BrandList(ListView):
    model = Brand
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))
    paginate_by = 20


class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug']) 
        return super().get_queryset().filter(brand=brand)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]

        return context
    

def add_review(request,slug):
    product = Product.objects.get(slug=slug)

    rate = request.POST['rate']   # rate = request.POST.get('rate')  
    review = request.POST['review']

    Review.objects.create(
        product = product ,
        rate = rate ,
        review = review , 
        user = request.user
    )

    # reviews
    reviews = Review.objects.filter(product=product)
    html = render_to_string('include/reviews_include.html',{'reviews':reviews})
    return JsonResponse({'result':html})


    # return redirect(f'/products/{product.slug}')