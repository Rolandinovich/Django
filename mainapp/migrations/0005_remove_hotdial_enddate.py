# Generated by Django 2.1.3 on 2018-12-08 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20181208_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotdial',
            name='enddate',
        ),
    ]