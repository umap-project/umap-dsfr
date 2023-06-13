from social_core.backends.open_id_connect import OpenIdConnectAuth


class MonComptePro(OpenIdConnectAuth):
    name = "moncomptepro"
    DEFAULT_SCOPE = ["openid", "profile", "email", "organizations"]
    USERNAME_KEY = "sub"
    EXTRA_DATA = ["id_token", "refresh_token", "organizations", "phone_number", "job", ("sub", "id")]
