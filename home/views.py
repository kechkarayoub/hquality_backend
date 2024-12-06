# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from utils.utils import (
    get_establishments_types_dict, get_establishments_users_accounts_types_dict, get_gender_choices_dict
)


