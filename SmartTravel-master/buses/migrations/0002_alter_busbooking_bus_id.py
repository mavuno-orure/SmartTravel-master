# Generated by Django 3.2.8 on 2021-10-13 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busbooking',
            name='bus_id',
            field=models.CharField(max_length=100),
        ),
    ]