# Generated by Django 4.2.1 on 2023-06-05 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_userprofile_perfildeusuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfildeusuario',
            name='email',
        ),
    ]
