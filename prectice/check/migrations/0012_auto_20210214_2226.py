# Generated by Django 3.1.4 on 2021-02-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0011_auto_20210214_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='bill_date',
            field=models.DateField(),
        ),
    ]