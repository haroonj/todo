# Generated by Django 3.1.5 on 2021-01-13 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Done'),
        ),
    ]
