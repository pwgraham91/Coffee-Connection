import flask
import flask_login
import json

from app import app, db
from app.lib.connection import generate_connections


@app.route('/api/connections/generate_connections', methods=['POST'])
def make_connections():
    session = db.session

    if not flask_login.current_user.is_authenticated:
        return 'Unauthorized', 403

    if not flask_login.current_user.admin:
        raise Exception('no access')

    generate_connections(session)
    session.commit()

    return flask.Response(json.dumps(flask_login.current_user.dict), mimetype=u'application/json')
