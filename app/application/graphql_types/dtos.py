import strawberry
from app.application.graphql_types.recipe import UnitMeasurement


@strawberry.input
class CreateIngredient:
    name: str
    quantity: float
    unit_measurement: UnitMeasurement
