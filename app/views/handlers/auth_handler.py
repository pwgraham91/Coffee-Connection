import flask

from requests_oauthlib import OAuth2Session

from config_director import Config


def get_google_auth(state=None, token=None):
    if token:
        return OAuth2Session(Config.Auth.CLIENT_ID, token=token)
    if state:
        return OAuth2Session(
            Config.Auth.CLIENT_ID,
            state=state,
            redirect_uri=Config.Auth.REDIRECT_URI,
            scope=['email']
        )
    oauth = OAuth2Session(
        Config.Auth.CLIENT_ID,
        redirect_uri=Config.Auth.REDIRECT_URI,
        scope=['email']
    )
    return oauth


def get_google_authorization_url():
    current_user = flask.g.user

    if current_user.is_authenticated:
        return

    google = get_google_auth()

    auth_url, state = google.authorization_url(Config.Auth.AUTH_URI)

    flask.session['oauth_state'] = state
    return auth_url
