# Generated by Django 2.0.13 on 2019-05-29 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20190529_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='read',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
