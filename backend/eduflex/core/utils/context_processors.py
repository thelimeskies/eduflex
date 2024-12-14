"""Django context processors."""

import environ

from constance import config

from django.conf import settings

from users.models import CustomUser

env = environ.FileAwareEnv()


def export_vars(request) -> dict:
    """Export environment variables to Django templates.

    https://stackoverflow.com/questions/43207563/how-can-i-access-environment-variables-directly-in-a-django-template/43211490#43211490?newreg=9f02cb1a210c4f618f41fb1759bd9fb3

    Useage
    ------

    An example of how to access the environment variable in the template using
    just the data dict key to pass the CSS file location to the template.

    
    <link rel="stylesheet" href="{{ CSS }}">
    

    """

    data: dict = {}

    data["PROJECT_NAME"] = "eduflex"

    

    
    # Passes environment and debug status to be displayed on webpage.
    match settings.SETTINGS_MODULE:
        case "config.settings.local":
            if settings.DEBUG:
                data["ENVIRONMENT"] = "LOCAL: Debug True"

            else:
                data["ENVIRONMENT"] = "LOCAL: Debug False"

        case "config.settings.production":
            data["ENVIRONMENT"] = "PRODUCTION"

        case "config.settings.staging":
            if settings.DEBUG:
                data["ENVIRONMENT"] = "STAGING: Debug True"
            else:
                data["ENVIRONMENT"] = "STAGING: Debug False"

        case "config.settings.test":
            if settings.DEBUG:
                data["ENVIRONMENT"] = "TESTING: Debug True"
            else:
                data["ENVIRONMENT"] = "TESTING: Debug False"

        case _:
            environ = settings.SETTINGS_MODULE.rsplit(".", 1)[-1].upper()

            if settings.DEBUG:
                data["ENVIRONMENT"] = f"{environ}: Debug True"
            else:
                data["ENVIRONMENT"] = f"{environ}: Debug False"
    
    
    data["ALLOW_NEW_USER_SIGNUP"] = config.ALLOW_NEW_USER_SIGNUP
    


    return data
