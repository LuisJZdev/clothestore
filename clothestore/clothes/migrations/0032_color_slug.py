# Generated by Django 4.1.5 on 2023-02-16 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0031_alter_clothingtype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]