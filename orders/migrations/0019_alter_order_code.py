# Generated by Django 4.2.5 on 2023-10-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='LI95RCHQ', max_length=20),
        ),
    ]
