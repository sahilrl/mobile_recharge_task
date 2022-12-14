from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from topup.models import PhoneNumberRegistrar, Plans


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumberRegistrar
        fields = '__all__' 



class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'