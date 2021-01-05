from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Create your models here.
class Customer(models.Model):
    class Meta:
        db_table = 'customer'
        managed = False

    customer_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    activebool = models.BooleanField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)


class Payment(models.Model):
    class Meta:
        db_table = 'payment'
        managed = False

    payment_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(primary_key=True)
    staff_id = models.IntegerField(null=True)
    rental_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(max_length=255, blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)


class Rental(models.Model):
    class Meta:
        db_table = 'rental'
        managed = False

    rental_id = models.IntegerField(blank=True, null=True)
    rental_date = models.DateTimeField(blank=True, null=True)
    inventory_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(primary_key=True)
    return_date = models.DateTimeField(blank=True, null=True)
    staff_id = models.IntegerField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)


class Inventory(models.Model):
    class Meta:
        db_table = 'inventory'
        managed = False

    inventory_id = models.IntegerField(blank=True, null=True)
    film_id = models.IntegerField(blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)


class Film(models.Model):
    class Meta:
        db_table = 'film'
        managed = False

    film_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    rental_duration = models.IntegerField(blank=True, null=True)
    rental_rate = models.FloatField(max_length=255, blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    replacement_cost = models.FloatField(max_length=255, blank=True, null=True)
    rating = models.CharField(max_length=255, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    special_features = models.TextField(max_length=255, blank=True, null=True)
    fulltext = models.CharField(max_length=255, primary_key=True)


class Address(models.Model):
    class Meta:
        db_table = 'address'
        managed = False

    address_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=20, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)


class Store(models.Model):
    class Meta:
        db_table = 'store'
        managed = False

    store_id = models.IntegerField(primary_key=True)
    manager_staff_id = models.IntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    last_update = models.DateTimeField(max_length=20, blank=True, null=True)


class Staff(models.Model):
    class Meta:
        db_table = 'staff'
        managed = False

    staff_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    picture = models.BinaryField(blank=True, null=True)