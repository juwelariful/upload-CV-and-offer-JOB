# Generated by Django 2.0.13 on 2019-02-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobcv', '0004_auto_20190219_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcircular',
            name='application_last_date',
            field=models.DateField(blank=True),
        ),
    ]
