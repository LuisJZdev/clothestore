# Generated by Django 4.1.5 on 2023-01-30 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0017_alter_pledge_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
            ],
        ),
    ]