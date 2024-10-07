import jwt
from social_core.backends.open_id_connect import OpenIdConnectAuth
from social_core.exceptions import AuthTokenError


class ProConnect(OpenIdConnectAuth):
    name = "proconnect"
    DEFAULT_SCOPE = ["openid", "profile", "email", "given_name", "usual_name"]
    USERNAME_KEY = "email"
    EXTRA_DATA = [
        "id_token",
        "refresh_token",
        "organization",
        "job",
        ("sub", "id"),
    ]

    def user_data(self, access_token, *args, **kwargs):
        # FIXME make a PR to social auth to deal with JWT when Content-Type reponse is
        # application/jwt, instead of trying to parse is as json
        client_id, client_secret = self.get_key_and_secret()
        headers = headers = {"Authorization": f"Bearer {access_token}"}
        token = self.request(self.userinfo_url(), headers=headers).text
        key = self.find_valid_key(token)
        if not key:
            raise AuthTokenError(self, "Signature verification failed")
        rsakey = jwt.PyJWK(key)
        return jwt.decode(
            token,
            rsakey.key,
            audience=client_id,
            algorithms=self.setting("JWT_ALGORITHMS", self.JWT_ALGORITHMS),
        )

    def get_user_details(self, response):
        details = super().get_user_details(response)
        details["last_name"] = response.get("usual_name")
        return details
