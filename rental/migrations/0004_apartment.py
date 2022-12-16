# Generated by Django 3.2.9 on 2022-12-16 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_auto_20221213_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=500)),
                ('description', models.TextField(blank=True, max_length=700, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('price_is_negotiable', models.BooleanField(default=True, help_text='can this price be negotiated')),
                ('number_of_rooms', models.PositiveIntegerField(max_length=2)),
                ('is_vacant', models.BooleanField(default=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rental.agent')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rental.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rental.country')),
                ('landlord', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rental.landlord')),
                ('lga', models.ForeignKey(help_text='local government area', on_delete=django.db.models.deletion.PROTECT, to='rental.lga')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rental.state')),
            ],
        ),
    ]
