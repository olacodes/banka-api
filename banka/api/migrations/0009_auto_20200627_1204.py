# Generated by Django 3.0.6 on 2020-06-27 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200627_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='cashier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
