# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.mail import send_mail
from pprint import pprint
from sib_api_v3_sdk.rest import ApiException
from django.utils.translation import gettext_lazy as _
import after_response
import base64, os
import datetime
import random
import requests
import sib_api_v3_sdk

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = os.getenv('BREVO_API_KEY')

# Create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))



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
def send_email(subject, message_txt, list_emails, html_message=None, names_by_emails={}):
    """
        :param subject: subject of the email
        :param message_txt: plain text of the email
        :param list_emails: list of receivers addresses of the email
        :param html_message: html_message of the email
        :return: None
    """
    if settings.EMAIL_SMTP_PROVIDER == "brevo":
        to_emails = [{"email": email, "name": names_by_emails.get(email) or ""} for email in list_emails]
        sender = {"name": settings.SITE_NAME, "email": os.getenv('EMAIL_FROM_ADDRESS')}
        return send_brevo_mail(subject, message_txt, sender, to_emails, html_message=html_message)
    else:
        return "no_smtp_email_provider"


def get_static_logo_url():
    """
        :return: the url of the website logo
    """
    return os.getenv('BACKEND_URL') + "/static/images/logo.jpg"


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


def send_brevo_mail(subject, message_txt, sender, to_emails, html_message=None, template_id=None):
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to_emails,
        sender=sender,
        subject=subject,
        html_content=html_message,  # Use this if not using a template
        template_id=template_id,  # Use this if using a template
    )

    try:
        # Send the email
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)


