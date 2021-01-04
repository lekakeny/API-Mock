# from django.contrib.auth.models import User, Group
import json
from abc import ABC

from rest_framework import serializers
# from mock.models import LANGUAGE_CHOICES, STYLE_CHOICES
from .models import Customer, Payment, Rental, Address, Film, Inventory, Store, Staff


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address',)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('customer_id', 'staff_id', 'rental_id')


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('title', 'description', 'rental_duration')


class StoreSerializer(serializers.ModelSerializer):
    store_id = serializers.IntegerField(read_only=True)
    manager_staff_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Store
        fields = ('store_id', 'manager_staff_id')


class CustomizedSerializer(serializers.Serializer):
    customer_name = serializers.SerializerMethodField(read_only=True)
    address = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(read_only=True)

    customer_id = serializers.IntegerField(read_only=True)
    staff_id = serializers.IntegerField(read_only=True)
    rental_id = serializers.IntegerField(read_only=True)
    payment = serializers.SerializerMethodField(read_only=True)

    film_section = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    rental_duration = serializers.IntegerField(read_only=True)

    store_section = serializers.SerializerMethodField(read_only=True)

    # store_section = serializers.SerializerMethodField(read_only=True)
    # store_id = serializers.IntegerField(read_only=True)
    # staff_manager_id = serializers.IntegerField(read_only=True)

    def get_customer_name(self, obj):
        return obj.first_name + " " + obj.last_name

    def get_staff_id(self, obj):
        return obj.staff_id

    def get_address(self, obj):
        qs = Address.objects.filter(address_id=obj.address_id).first().address
        return qs
        # data_result = []
        # for i in qs: data_result.append(i.address)
        # return data_result

    # get_ + variable name
    def get_payment(self, obj):
        qs = Payment.objects.filter(customer_id=obj.customer_id).all()
        sr = PaymentSerializer(qs, many=True).data
        return sr

    def get_film_section(self, obj):
        # qs = Rental.objects.filter(customer_id=obj.customer_id).all()
        # qs = Inventory.objects.filter(inventory_id=obj.inventory_id).all()
        qs = Film.objects.filter(film_id=obj.customer_id).all()
        sr = FilmSerializer(qs, context={Rental.customer_id: Customer.customer_id,
                                         Inventory.inventory_id: Rental.inventory_id,
                                         Film.film_id: Inventory.film_id},
                            many=True).data
        return sr

    def get_store_section(self, obj):
        qs = Store.objects.filter(store_id=obj.customer_id).all()
        sr = StoreSerializer(qs,
                             context={Customer.customer_id: Rental.customer_id,
                                      Rental.staff_id: Staff.staff_id,
                                      Staff.store_id: Store.store_id,
                                      },
                             many=True).data
        return sr

# with open('CustomizedSerializer.json', 'w') as fp:
#     json.dump(CustomizedSerializer, fp, sort_keys=False, indent=4)
