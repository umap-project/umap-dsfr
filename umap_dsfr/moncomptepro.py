from social_core.backends.open_id_connect import OpenIdConnectAuth


class MonComptePro(OpenIdConnectAuth):
    name = "moncomptepro"
    DEFAULT_SCOPE = ["openid", "profile", "email", "organizations"]
    USERNAME_KEY = "sub"
    EXTRA_DATA = ["id_token", "refresh_token", "organizations", "phone_number", "job", ("sub", "id")]

    def auth_allowed(self, response, details):
        for org in response.get("organizations", []):
            if org["is_collectivite_territoriale"] or org["is_service_public"]:
                # TODO should we check for is_external ?
                return True
        return False
