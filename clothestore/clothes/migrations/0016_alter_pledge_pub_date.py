# Generated by Django 4.1 on 2022-08-10 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0015_alter_pledge_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 10, 15, 59, 48, 333050, tzinfo=datetime.timezone.utc)),
        ),
    ]
