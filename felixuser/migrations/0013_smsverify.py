# Generated by Django 2.0.13 on 2019-06-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('felixuser', '0012_auto_20190529_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsVerify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=12, verbose_name='Номер менеджера')),
                ('code', models.IntegerField(verbose_name='Проверочный код')),
            ],
            options={
                'verbose_name': 'Проверочный код',
                'verbose_name_plural': 'Проверочные коды',
            },
        ),
    ]
