# Generated by Django 2.0.10 on 2019-02-20 16:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_auto_20190220_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=datetime.datetime(2019, 2, 20, 16, 49, 4, 741768, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='page_permission',
            field=models.CharField(choices=[('a', 'allow'), ('d', 'deny')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
