from admin_backend.models import User


def get_user_by_id(user_id):
    user = User.query.filter(User.id == user_id).first()
    return user


def load_user(user_id):
    return get_user_by_id(user_id)
