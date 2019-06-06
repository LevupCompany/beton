# Generated by Django 2.0.13 on 2019-05-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('felixuser', '0011_auto_20190527_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='zones', to='felixuser.Notification'),
        ),
    ]