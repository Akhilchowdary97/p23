# Generated by Django 3.0 on 2020-09-07 11:04

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[myapp.models.validate_name]),
        ),
    ]
