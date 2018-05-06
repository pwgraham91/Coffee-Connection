import json

import flask

from app import app, db
from app.models import User


@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    session = db.session

    user = session.query(User).get(user_id)
    if not user:
        return 'User {} not found'.format(user_id), 404

    return flask.Response(json.dumps(user.dict), mimetype=u'application/json')
