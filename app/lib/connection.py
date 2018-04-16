import random

import datetime

from app.models import User, Connection


def get_available_connections(available_user_ids, user):
    """
    takes a list of active user ids and a user and returns a list of available user ids
    :param available_user_ids: Set of integers
    :param user: User
    :return Set: modified copy of original available_user_ids
    """
    available_user_ids_copy = available_user_ids.copy()

    # This line is sort of redundant because we remove the current user from chosen_user_ids in generate_connections
    # but we need that line to make sure we don't add the user as a user_2 connection as well. We need this line here
    # to make the function reusable and make sense.
    available_user_ids_copy.discard(user.id)

    for previous_connection in user.user_1s:
        available_user_ids_copy.discard(previous_connection.user_2.id)

    for previous_connection in user.user_2s:
        available_user_ids_copy.discard(previous_connection.user_1.id)

    return available_user_ids_copy


def generate_connections(session):
    """ Iterate through all users and generate connections. Each connection made should include users who have never
        been connected before.
    """
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

        available_user_ids = get_available_connections(active_user_ids - chosen_user_ids, user)

        if len(available_user_ids) == 0:
            continue

        user_2_id = random.choice(list(available_user_ids))
        chosen_user_ids.update({user_2_id})

        cxn = Connection(user_1=user, user_2_id=user_2_id, created_at=datetime.datetime.utcnow())
        session.add(cxn)
