# Generated by Django 3.0.5 on 2022-05-06 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_auto_20220506_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toppings',
            name='topping_name',
            field=models.TextField(null=True),
        ),
    ]
