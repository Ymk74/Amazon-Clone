# Generated by Django 4.2.5 on 2023-10-07 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='2K8WDDFC', max_length=20),
        ),
    ]
