# Generated by Django 4.2.5 on 2023-10-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_product_orderdetail_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='PAUMRTAV', max_length=20),
        ),
    ]
