# Generated by Django 3.2.20 on 2023-08-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votecard',
            name='description',
            field=models.TextField(max_length=264),
        ),
    ]
