# -*- coding: utf-8 -*-

from django.conf import settings
from django.test import TestCase
from user.models import Establishment, EstablishmentUser
import json


class HomeViewsTest(TestCase):

    def test_general_information_api(self):
        response = self.client.get('/general_information_api', {}, follow=True)
        json_response = json.loads(response.content)
        self.assertTrue(json_response.get("success"))
        self.assertEqual(json_response.get("general_information").get("site_name"), settings.SITE_NAME)
        self.assertEqual(json_response.get("general_information").get("contact_email"), settings.CONTACT_EMAIL)
        self.assertEqual(len(json_response.get("general_information").keys()), 2)

    def test_configuration_api_get(self):
        response = self.client.get('/configuration_api_get', {}, follow=True)
        json_response = json.loads(response.content)
        self.assertTrue(json_response.get("success"))
        self.assertEqual(len(json_response.get("establishments_types_dict")), len(Establishment.TYPES_DICT.keys()))
        self.assertEqual(len(json_response.get("establishments_users_accounts_types_dict")), len(EstablishmentUser.ACCOUNT_TYPES_DICT.keys()))
        self.assertEqual(len(json_response.get("gender_choices_dict")), len(EstablishmentUser.GENDERS_DICT.keys()))

