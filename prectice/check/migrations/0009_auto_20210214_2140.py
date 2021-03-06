# Generated by Django 3.1.4 on 2021-02-14 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0008_auto_20210214_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('allot_date', models.DateField()),
                ('Nurses', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='check.nurses')),
            ],
        ),
        migrations.CreateModel(
            name='attend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Doctors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='check.doctors')),
                ('Patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='check.patient')),
            ],
        ),
        migrations.AddField(
            model_name='admitted',
            name='Room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='check.room'),
        ),
        migrations.AddField(
            model_name='patient',
            name='Bill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='check.bill'),
        ),
    ]
