# Generated by Django 4.2.5 on 2023-10-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_rename_product_cartdetail_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdetail',
            old_name='product',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='total_after_coupon',
            new_name='total_After_coupon',
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='NJBEFZL1', max_length=20),
        ),
    ]