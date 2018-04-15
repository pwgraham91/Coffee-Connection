import random

import datetime

from app.models import User, Connection


def discard_previous_connections_from_set(available_user_ids, user):
    """
    Iterate through each of the users previous connections and remove the user ids from set of available ids.

    :param available_user_ids: set of integers
    :param user: User
    :return Set: modified copy of original available_user_ids
    """
    available_user_ids_copy = available_user_ids.copy()

    for previous_connection in user.user_1s:
        available_user_ids_copy.discard(previous_connection.user_2.id)

    for previous_connection in user.user_2s:
        available_user_ids_copy.discard(previous_connection.user_1.id)

    return available_user_ids_copy


def generate_connections(session):
    active_users = session.query(User).filter(
        User.active.is_(True)
    ).all()

    active_user_ids = {user.id for user in active_users}
    chosen_user_ids = set()

    for user in active_users:
        if user.id in chosen_user_ids:
            # if a user has been chosen for a connection, skip them
            continue

        # this user will be chosen as user_1 for this connection, add them to the chosen list
        chosen_user_ids.update({user.id})

        available_user_ids = discard_previous_connections_from_set(active_user_ids - chosen_user_ids, user)

        if len(available_user_ids) == 0:
            continue

        user_2_id = random.choice(list(available_user_ids))
        chosen_user_ids.update({user_2_id})

        cxn = Connection(user_1=user, user_2_id=user_2_id, created_at=datetime.datetime.utcnow())
        session.add(cxn)
