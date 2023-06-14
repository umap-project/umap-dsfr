# uMap-DSFR

## Installation

    pip install git+https://github.com/umap-project/umap-dsfr


## Configuration

In your local settings, add the `umap_dsfr` app:

    from umap.settings.base import *

    INSTALLED_APPS = (
        "umap_anct",
    ) + INSTALLED_APPS


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
