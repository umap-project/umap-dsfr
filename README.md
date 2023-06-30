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

And set the correct number of results per search:

    UMAP_MAPS_PER_SEARCH = 24

Add MonComptePro settings:

    # For testing
    SOCIAL_AUTH_MONCOMPTEPRO_OIDC_ENDPOINT = "https://app-test.moncomptepro.beta.gouv.fr"
    # For production
    SOCIAL_AUTH_MONCOMPTEPRO_OIDC_ENDPOINT = "https://app.moncomptepro.beta.gouv.fr"
    SOCIAL_AUTH_MONCOMPTEPRO_KEY = "xxxxx"
    SOCIAL_AUTH_MONCOMPTEPRO_SECRET = "xxxx"

    AUTHENTICATION_BACKENDS = (
        'umap_dsfr.moncomptepro.MonComptePro',
        'django.contrib.auth.backends.ModelBackend',
    )

Set the correct user-related settings:

    USER_DISPLAY_NAME = "{first_name} {last_name}"
    USER_AUTOCOMPLETE_FIELDS = ["^email"]
    USER_URL_FIELD = "pk"
