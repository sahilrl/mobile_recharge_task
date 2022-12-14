from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from topup import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('phone/', views.PhoneNumberList.as_view()),
    path('plans/', views.PlansList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
