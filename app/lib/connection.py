import random

import datetime

from app.models import User, Connection


def generate_connections(session):
    active_users = session.query(User).filter(
        User.active.is_(True)
    ).all()

    active_user_ids = {user.id for user in active_users}
    chosen_user_ids = set()

    for user in active_users:
        if user.id in chosen_user_ids:
            continue
        chosen_user_ids.update({user.id})

        available_user_ids = active_user_ids.copy()
        available_user_ids = available_user_ids - chosen_user_ids

        for previous_connection in user.user_1s:
            available_user_ids.discard(previous_connection.user_2.id)

        for previous_connection in user.user_2s:
            available_user_ids.discard(previous_connection.user_1.id)

        if len(available_user_ids) == 0:
            continue

        user_2_id = random.choice(list(available_user_ids))
        chosen_user_ids.update({user_2_id})

        cxn = Connection(user_1=user, user_2_id=user_2_id)
        cxn.created_at = datetime.datetime.utcnow()
        session.add(cxn)
