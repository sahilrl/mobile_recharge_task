from django.db import models


class PhoneNumberRegistrar(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    country_code = models.CharField(max_length=10)
    phone_number = models.IntegerField(max_length=10)

 

class Plans(models.Model):
    plan_name = models.CharField(max_length=500)
    description = models.TextField()
    amount = models.IntegerField()
    validity = models.IntegerField() # 0 for unlimited
    data_gb = models.IntegerField()
    sms = models.CharField()


class recharge(models.Model):
    customer_phone_id = models.ForeignKey(PhoneNumberRegistrar, null=False, blank=False, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Plans, null=False, blank=False, on_delete=models.CASCADE)
    recharge_date = models.DateTimeField(null=False, blank=False) # validity starts from

