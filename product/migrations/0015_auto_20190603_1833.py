# Generated by Django 2.0.13 on 2019-06-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20190529_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/banner/{user}', verbose_name='Акция'),
        ),
    ]