from django.apps import AppConfig as DjangoAppConfig

from edc_lab.apps import AppConfig as EdcLabAppConfigParent
from edc_registration.apps import AppConfig as EdcRegistrationAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'example'


class EdcRegistrationAppConfig(EdcRegistrationAppConfigParent):
    app_label = 'example'
    subject_types = ['subject']
    max_subjects = {'subject': -1}


class EdcLabAppConfig(EdcLabAppConfigParent):
    app_label = 'example'
