from topup.models import PhoneNumberRegistrar, Plans
from topup.serializers import PhoneNumberSerializer, PlansSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics


class PhoneNumberList(generics.ListCreateAPIView):
    """
    List all phonenumbers, or create a new phonenumber.
    """
    queryset = PhoneNumberRegistrar.objects.all()
    serializer_class = PhoneNumberSerializer



class PlansList(generics.ListCreateAPIView):
    """
    CRUD API for Plans
    """
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer