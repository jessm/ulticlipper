# Generated by Django 4.1.1 on 2022-09-30 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clip',
            options={},
        ),
        migrations.RemoveField(
            model_name='clip',
            name='upload_date',
        ),
    ]
