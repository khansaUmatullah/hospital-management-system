# Generated by Django 3.1.4 on 2021-02-14 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0006_auto_20210211_0336'),
    ]

    operations = [
        migrations.CreateModel(
            name='admitted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admitteddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('phoneno', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=10)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='nurses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('phoneno', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=20)),
                ('Employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='check.employee')),
            ],
        ),
        migrations.CreateModel(
            name='receiptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('phoneno', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=20)),
                ('Employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='check.employee')),
            ],
        ),
        migrations.CreateModel(
            name='visited',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visiteddate', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Team',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='image',
        ),
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='b_group',
            field=models.TextField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='team',
        ),
        migrations.AddField(
            model_name='visited',
            name='Patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='check.patient'),
        ),
        migrations.AddField(
            model_name='doctors',
            name='Employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='check.employee'),
        ),
        migrations.AddField(
            model_name='admitted',
            name='Patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='check.patient'),
        ),
    ]