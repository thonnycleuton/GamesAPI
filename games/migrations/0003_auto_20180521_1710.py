# Generated by Django 2.0.5 on 2018-05-21 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20180521_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='score_data',
            new_name='score_date',
        ),
    ]
