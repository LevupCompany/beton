# Generated by Django 2.0.13 on 2019-05-31 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20190529_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='min_price',
            field=models.IntegerField(default=100, verbose_name='Минимальная цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='weight',
            field=models.IntegerField(blank=True, verbose_name='Объем'),
        ),
    ]
