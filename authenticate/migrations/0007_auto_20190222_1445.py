# Generated by Django 2.0.10 on 2019-02-22 08:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0006_auto_20190222_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(default=datetime.datetime(2019, 2, 22, 8, 45, 38, 687022, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(max_length=200),
        ),
    ]
