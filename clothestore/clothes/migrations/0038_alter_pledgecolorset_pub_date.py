# Generated by Django 4.1.5 on 2023-04-17 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0037_alter_pledgecolorset_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledgecolorset',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 14, 57, 13, 687582, tzinfo=datetime.timezone.utc)),
        ),
    ]