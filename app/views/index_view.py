import flask

from app import app
from app.views.handlers.auth_handler import get_google_authorization_url


@app.route('/')
@app.route('/index')
@app.route('/profile/<int:profile_id>')
def index(profile_id=None):
    # configure flask to take all 404s and render index. then in react, render a 404 if it's not found from there
    user = flask.g.user
    return flask.render_template('index.html',
                                 user=user,
                                 auth_url=get_google_authorization_url())
