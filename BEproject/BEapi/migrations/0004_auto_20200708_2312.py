# Generated by Django 3.0.8 on 2020-07-08 23:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BEapi', '0003_auto_20200708_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskduedate',
            field=models.DateField(verbose_name=datetime.datetime(2020, 7, 8, 23, 12, 26, 482354, tzinfo=utc)),
        ),
    ]
