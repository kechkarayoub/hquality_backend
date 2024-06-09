from django.urls import path

from . import views

urlpatterns = [
    path('configuration_api_get', views.configuration_api_get, name='configuration_api_get'),
    path('general_information_api/', views.general_information_api, name="general_information_api"),
]
