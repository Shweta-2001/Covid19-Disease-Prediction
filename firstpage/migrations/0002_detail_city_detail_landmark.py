# Generated by Django 4.0.3 on 2022-06-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='landmark',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
