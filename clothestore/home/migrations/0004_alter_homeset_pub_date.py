# Generated by Django 4.1.5 on 2023-04-17 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homeset_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeset',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 14, 29, 38, 479217, tzinfo=datetime.timezone.utc)),
        ),
    ]
