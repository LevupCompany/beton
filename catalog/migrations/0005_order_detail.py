# Generated by Django 2.2 on 2019-05-15 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190515_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='detail',
            field=models.TextField(default='', verbose_name='Детали заказа'),
        ),
    ]
