# Generated by Django 3.0.6 on 2020-06-11 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200611_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='status',
            new_name='account_status',
        ),
    ]
