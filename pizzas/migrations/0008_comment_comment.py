# Generated by Django 3.0.5 on 2022-05-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
