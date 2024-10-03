# uMap-DSFR

## Installation

    pip install git+https://github.com/umap-project/umap-dsfr
    make jsinstall
    make dsfr-lite


## Configuration

In your local settings, add the `umap_dsfr` app:

    from umap.settings.base import *

    INSTALLED_APPS = (
        "umap_dsfr",
    ) + INSTALLED_APPS


Set the custom url conf:

    ROOT_URLCONF = "umap_dsfr.urls"

And set the correct number of results per search:

    UMAP_MAPS_PER_SEARCH = 24

Add ProConnect settings:

    # For testing
    SOCIAL_AUTH_PROCONNECT_OIDC_ENDPOINT = "https://app-test.proconnect.beta.gouv.fr"
    # For production
    SOCIAL_AUTH_PROCONNECT_OIDC_ENDPOINT = "https://app.proconnect.beta.gouv.fr"
    SOCIAL_AUTH_PROCONNECT_KEY = "xxxxx"
    SOCIAL_AUTH_PROCONNECT_SECRET = "xxxx"

    AUTHENTICATION_BACKENDS = (
        'umap_dsfr.proconnect.ProConnect',
        'django.contrib.auth.backends.ModelBackend',
    )

Set the correct user-related settings:

    USER_DISPLAY_NAME = "{first_name} {last_name}"
    USER_AUTOCOMPLETE_FIELDS = ["^email"]
    USER_URL_FIELD = "pk"
