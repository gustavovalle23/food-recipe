import strawberry
from app.application.graphql_types.recipe import UnitMeasurement


@strawberry.input
class CreateIngredient:
    name: str
    quantity: float
    unit_measurement: UnitMeasurement


@strawberry.input
class CreateRecipe:
    name: str
    link: str


@strawberry.input
class LoginInput:
    username: str
    password: str
