# Generated by Django 3.2.9 on 2022-12-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0013_auto_20221223_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='lga',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
