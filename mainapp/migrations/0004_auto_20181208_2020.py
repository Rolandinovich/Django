# Generated by Django 2.1.3 on 2018-12-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20181208_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotdial',
            name='enddate',
            field=models.DateField(auto_now_add=True),
        ),
    ]