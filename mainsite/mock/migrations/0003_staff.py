# Generated by Django 2.2.16 on 2020-12-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mock', '0002_address_film_inventory_payment_rental_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address_id', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('store_id', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(blank=True, max_length=20, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('picture', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'staff',
                'managed': False,
            },
        ),
    ]