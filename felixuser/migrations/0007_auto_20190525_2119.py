# Generated by Django 2.0.13 on 2019-05-25 18:19

from django.db import migrations, models
import felixuser.models


class Migration(migrations.Migration):

    dependencies = [
        ('felixuser', '0006_auto_20190524_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='logo',
            field=models.ImageField(blank=True, height_field=150, upload_to=felixuser.models.get_upload_path2, verbose_name='Лого компании', width_field=150),
        ),
    ]
