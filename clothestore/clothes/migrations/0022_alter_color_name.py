# Generated by Django 4.1.5 on 2023-01-31 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0021_remove_pledge_image_remove_pledge_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
