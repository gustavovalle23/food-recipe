import strawberry


@strawberry.input
class IngredientDto:
    name: str
    quantity: float
