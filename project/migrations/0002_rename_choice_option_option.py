# Generated by Django 4.0 on 2021-12-28 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='choice',
            new_name='option',
        ),
    ]
