# Generated by Django 3.1.4 on 2021-01-27 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_auto_20210128_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]