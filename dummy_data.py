import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random 
from product.models import Brand , Product




def seed_brand(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpeg','4.jpg','5.png','6.jpg','7.png','8.png','9.jpg','10.png']
    for _ in range(n):
        Brand.objects.create(
            name = fake.name() ,
            image = f'brands/{images[random.randint(0,9)]}',
        )
    print(f'Seed {n} Brands Succesfully ')


def seed_product(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpeg','4.jpg','5.png','6.jpg','7.png','8.png','9.jpg','10.png']
    flags = ['New','Sale','Feature']
    
    for _ in range(n):
        Product.objects.create(
        name = fake.name() ,
        image = f'brands/{images[random.randint(0,9)]}',
        flag = flags[random.randint(0,2)],
        price = round(random.uniform(20.99,99.99),2),
        sku = random.randint(1000,1000000),
        subtitle = fake.text(max_nb_chars=250),
        description = fake.text(max_nb_chars=2000),
        quantity = random.randint(0,30),
        brand = Brand.objects.get(id=random.randint(1,105)),
        )
    print(f'Seed {n} Product Succesfully ')




# seed_brand(100)
seed_product(2000)

