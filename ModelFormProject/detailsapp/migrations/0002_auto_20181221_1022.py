# Generated by Django 2.0.3 on 2018-12-21 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detailsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='gender',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='userdetails',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='userdetails',
            old_name='notes',
            new_name='state',
        ),
    ]