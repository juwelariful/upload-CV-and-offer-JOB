# Generated by Django 2.0.10 on 2019-02-22 14:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobcv', '0006_auto_20190220_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='publish_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cv',
            name='file',
            field=models.FileField(upload_to='cv/'),
        ),
        migrations.AlterField(
            model_name='jobcircular',
            name='job_nature',
            field=models.CharField(max_length=9),
        ),
    ]
