import flask
import flask_login
import json

from app import app, db


@app.route('/api/connections/generate_connections', methods=['POST'])
def make_connections():
    session = db.session

    if not flask_login.current_user.is_authenticated:
        return 'Unauthorized', 403

    if not flask_login.current_user.admin:
        # todo generate connections here based on users who haven't connected yet and are available for connection
        raise Exception('no access')
    return flask.Response(json.dumps({
        'success': True
    }), mimetype=u'application/json')
