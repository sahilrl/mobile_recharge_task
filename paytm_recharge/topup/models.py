"""In real world there may be multiple seperate apps for PhoneNumberRegistrar, Plans and Recharge.
Since it's just a demo task, I'm including everything in one app."""
from django.db import models


class PhoneNumberRegistrar(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    country_code = models.CharField(max_length=10, default="+91", blank=True, null=True)
    phone_number = models.IntegerField()

    def __str__(self):
        return (self.first_name +" " +str(self.phone_number))

 

class Plans(models.Model):
    TIME = [
        (0, 'Day'),
        (1, 'Month'),
        (2, 'Year'),
    ]
    plan_name = models.CharField(max_length=500)
    description = models.TextField()
    amount = models.IntegerField()
    validity = models.IntegerField() # 0 for unlimited
    data_gb = models.IntegerField()
    data_per = models.IntegerField(choices=TIME, default=1) # data 2BG internet per day or month?
    sms = models.IntegerField()
    sms_per = models.IntegerField(choices=TIME, default=1) # sms 50 sms per day or month?

    def __str__(self):
        return self.plan_name

class Recharge(models.Model):
    customer_phone_id = models.ForeignKey(PhoneNumberRegistrar, null=False, blank=False, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Plans, null=False, blank=False, on_delete=models.CASCADE)
    recharge_date = models.DateTimeField(null=False, blank=False) # validity starts from