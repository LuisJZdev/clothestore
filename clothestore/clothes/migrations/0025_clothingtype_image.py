# Generated by Django 4.1.5 on 2023-01-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0024_alter_pledge_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothingtype',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]