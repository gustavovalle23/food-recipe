import strawberry


@strawberry.type
class User:
	name: str
	email: str
	birth_date: str
