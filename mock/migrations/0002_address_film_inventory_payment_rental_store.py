# Generated by Django 2.2.16 on 2020-12-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('address2', models.CharField(blank=True, max_length=255, null=True)),
                ('district', models.CharField(blank=True, max_length=20, null=True)),
                ('city_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('film_id', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('release_year', models.IntegerField(blank=True, max_length=255, null=True)),
                ('language_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('rental_duration', models.IntegerField(blank=True, max_length=255, null=True)),
                ('rental_rate', models.FloatField(blank=True, max_length=255, null=True)),
                ('length', models.IntegerField(blank=True, max_length=255, null=True)),
                ('replacement_cost', models.FloatField(blank=True, max_length=255, null=True)),
                ('rating', models.CharField(blank=True, max_length=255, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('special_features', models.TextField(blank=True, max_length=255, null=True)),
                ('fulltext', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'film',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('film_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('store_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'inventory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('customer_id', models.IntegerField(max_length=255, primary_key=True, serialize=False)),
                ('staff_id', models.IntegerField(null=True)),
                ('rental_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('amount', models.FloatField(blank=True, max_length=255, null=True)),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('rental_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('rental_date', models.DateTimeField(blank=True, null=True)),
                ('inventory_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('customer_id', models.IntegerField(max_length=255, primary_key=True, serialize=False)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('staff_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rental',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('manager_staff_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('address_id', models.IntegerField(blank=True, max_length=255, null=True)),
                ('last_update', models.DateTimeField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'store',
                'managed': False,
            },
        ),
    ]
