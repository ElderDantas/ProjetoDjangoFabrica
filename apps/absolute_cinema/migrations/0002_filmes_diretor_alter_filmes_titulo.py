# Generated by Django 5.1 on 2024-08-24 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absolute_cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmes',
            name='diretor',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filmes',
            name='titulo',
            field=models.CharField(max_length=40),
        ),
    ]
