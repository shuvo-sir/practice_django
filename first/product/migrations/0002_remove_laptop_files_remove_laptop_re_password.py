# Generated by Django 4.2 on 2023-05-16 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='files',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='re_password',
        ),
    ]