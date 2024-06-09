# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
import after_response
import base64
import datetime
import random
import requests


BG_COLORS_CHOICES = ["#f36422", "#ffee02", "#f070a9", "#00adef", "#7cc142", "#d02b49"]


def get_random_bg_color():
    return random.choice(BG_COLORS_CHOICES)


def date_from_string(date_string):
    """
        :param date_string: date string from the user request
        :return: return a date object if the string match "%d/%m/%Y" format else return None
    """
    try:
        return datetime.datetime.strptime(date_string, "%d/%m/%Y")
    except:
        return None


@after_response.enable
def send_email(subject, message_txt, list_emails, html_message=None):
    """
        :param subject: subject of the email
        :param message_txt: plain text of the email
        :param list_emails: list of receivers addresses of the email
        :param html_message: html_message of the email
        :return: None
    """
    if settings.EMAIL_SMTP_PROVIDER == "sendgrid":
        return send_mail(subject, message_txt, settings.EMAIL_FROM_ADDRESS, list_emails, html_message=html_message)
    else:
        return "no_smtp_email_provider"


def get_static_logo_url():
    """
        :return: the url of the website logo
    """
    return settings.BACKEND_URL + "/static/images/logo.jpg"


def get_img_as_base64(url):
    """
        :param url: image url
        :return: convert the image url to base64 encode
    """
    return base64.b64encode(requests.get(url).content).decode('ascii')



def get_establishments_types():
    """
        :params: None
        :return: A tuple of tuples of establishment type's key and value
    """
    return (
        ("hospital", _("Hospital")),
        ("laboratory", _("Laboratory")),
    )


def get_establishments_types_dict():
    """
        :params: None
        :return: A dictionary with keys values are establishment type's key and value
    """
    establishments_types = get_establishments_types()
    establishments_types_dict = {}
    for establishment_type in establishments_types:
        establishments_types_dict[establishment_type[0]] = establishment_type[1]
    return establishments_types_dict


def get_establishments_users_accounts_types():
    """
        :params: None
        :return: A tuple of tuples of establishment user type's key and value
    """
    return (
        ("assistant", _("Assistant")),
        ("doctor", _("Doctor")),
        ("director", _("Director")),
        ("nurse", _("Nurse")),
        ("patient", _("Patient")),
        ("technician", _("Technician")),
        ("other", _("Other")),
    )


def get_establishments_users_accounts_types_dict():
    """
        :params: None
        :return: A dictionary with keys values are establishment user type's key and value
    """
    establishments_users_accounts_types = get_establishments_users_accounts_types()
    establishments_users_accounts_types_dict = {}
    for e_u_a_t in establishments_users_accounts_types:
        establishments_users_accounts_types_dict[e_u_a_t[0]] = e_u_a_t[1]
    return establishments_users_accounts_types_dict


def get_gender_choices():
    """
        :params: None
        :return: A tuple of tuples of gender's key and value
    """
    return (
        ("", _("Select")),
        ("f", _("Female")),
        ("m", _("Male")),
    )


def get_gender_choices_dict():
    """
        :params: None
        :return: A dictionary with keys values are gender's key and value
    """
    gender_choices = get_gender_choices()
    gender_choices_dict = {}
    for gender_choice in gender_choices:
        gender_choices_dict[gender_choice[0]] = gender_choice[1]
    return gender_choices_dict