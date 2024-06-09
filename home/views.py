# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from utils.utils import (
    get_establishments_types_dict, get_establishments_users_accounts_types_dict, get_gender_choices_dict
)


@api_view(['GET'])
def configuration_api_get(request):
    """
        :param request: user request
        :return: system configuration
    """
    response = JsonResponse({
        "establishments_types_dict": get_establishments_types_dict(),
        "establishments_users_accounts_types_dict": get_establishments_users_accounts_types_dict(),
        "gender_choices_dict": get_gender_choices_dict(),
        "success": True,
    })
    return response


@api_view(['GET'])
def general_information_api(request):
    """
        :param request: user request
        :return: general information of the website
    """
    response = JsonResponse({
        "general_information": {
            "site_name": settings.SITE_NAME,
            "contact_email": settings.CONTACT_EMAIL,
        },
        "success": True,
    })
    return response
