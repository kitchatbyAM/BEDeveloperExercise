# Generated by Django 3.0.8 on 2020-07-09 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BEapi', '0007_auto_20200709_0047'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TaskSerializer',
        ),
        migrations.AlterField(
            model_name='task',
            name='taskduedate',
            field=models.DateTimeField(),
        ),
    ]