# Generated by Django 4.1.5 on 2023-02-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeset',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
