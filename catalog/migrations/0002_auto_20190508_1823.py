# Generated by Django 2.2 on 2019-05-08 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(upload_to='static/images', verbose_name='Иконка'),
        ),
    ]
