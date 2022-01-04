# Generated by Django 3.2.6 on 2021-08-25 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='datetime'),
            preserve_default=False,
        ),
    ]