# Generated by Django 3.2.9 on 2022-12-23 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0008_country_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.UUIDField(default='f94eeb', editable=False, primary_key=True, serialize=False),
        ),
    ]