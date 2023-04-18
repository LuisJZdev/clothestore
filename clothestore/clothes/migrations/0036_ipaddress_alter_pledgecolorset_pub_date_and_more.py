# Generated by Django 4.1.5 on 2023-04-17 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0035_alter_pledgecolorset_pub_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
        migrations.AlterField(
            model_name='pledgecolorset',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 14, 51, 36, 332655, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='PledgeColorSetVisualisation',
        ),
    ]