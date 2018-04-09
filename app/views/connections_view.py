import flask
from flask_login import login_required

from app import app, db


@app.route('/make_connections', methods=['POST'])
@login_required
def make_connections():
    session = db.session
    current_user = flask.g.user

    if not current_user.is_admin:
        raise Exception('no access')