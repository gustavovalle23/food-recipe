from schemas.users import User


def get_users():
    return [
        User(
			name='Gustavo Valle',
			birth_date='10-12-1996',
			email='gustavo@gmail.com'
        ),
    ]
