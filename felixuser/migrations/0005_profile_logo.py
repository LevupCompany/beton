# Generated by Django 2.0.13 on 2019-05-24 17:07

from django.db import migrations, models
import felixuser.models


class Migration(migrations.Migration):

    dependencies = [
        ('felixuser', '0004_auto_20190511_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='logo',
            field=models.ImageField(blank=True, upload_to=felixuser.models.get_upload_path, verbose_name='Лого компании'),
        ),
    ]