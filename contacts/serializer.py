from rest_framework import serializers

from contacts.models import Contact,ContactPhone,ContactEmail


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields="__all__"


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactPhone
        fields="__all__"


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactEmail
        fields="__all__"


class NewContactSerializer(serializers.Serializer):
    firstName = serializers.CharField(required=True,allow_blank=False,allow_null=False,min_length=3)
    lastName= serializers.CharField(required=False,allow_blank=False,allow_null=False,min_length=3)
    uuid = serializers.CharField(required=False,allow_blank=True,allow_null=True)


class NewPhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True,allow_blank=True,allow_null=True)
    contact_uuid=serializers.CharField(required=False,allow_blank=True,allow_null=True)


class NewEmailSerializer(serializers.Serializer):
    email = serializers.CharField(required=True,allow_blank=True,allow_null=True)
    contact_uuid=serializers.CharField(required=False,allow_blank=True,allow_null=True)