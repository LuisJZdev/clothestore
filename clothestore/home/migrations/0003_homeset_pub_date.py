# Generated by Django 4.1.5 on 2023-02-16 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_homeset_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeset',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 16, 10, 47, 54, 347130, tzinfo=datetime.timezone.utc)),
        ),
    ]
