from social_core.backends.open_id_connect import OpenIdConnectAuth


class MonComptePro(OpenIdConnectAuth):
    name = "moncomptepro"
    DEFAULT_SCOPE = ["openid", "profile", "email", "organization"]
    USERNAME_KEY = "sub"
    EXTRA_DATA = [
        "id_token",
        "refresh_token",
        "organization",
        "job",
        ("sub", "id"),
    ]

    def auth_allowed(self, response, details):
        if response.get("is_commune") or response.get("is_service_public"):
            # TODO should we check for is_external ?
            return True
        return False
