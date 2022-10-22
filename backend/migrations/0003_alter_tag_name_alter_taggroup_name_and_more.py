# Generated by Django 4.1.1 on 2022-10-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_tag_backend_tag_name_194adf_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='taggroup',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='youtube_id',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]