from typing import List
from app.infra.models import Ingredient as SchemaIngredient, Recipe as SchemaRecipe
from app.graphql_types.recipe import Ingredient, Recipe, UnitMeasurement


class IngredientBuilder:
    @staticmethod
    def buid_one(ingredient: SchemaIngredient) -> Ingredient:

        return Ingredient(
            name=ingredient.name,
            quantity=ingredient.quantity,
            unit_measurement=UnitMeasurement(ingredient.unit_measurement.value)
        )

    @staticmethod
    def buid_list(ingredients_db: List[SchemaIngredient]) -> List[Ingredient]:
        ingredients = []
        for ingredient in ingredients_db:
            ingredients.append(Ingredient(
                name=ingredient.name,
                quantity=ingredient.quantity,
                unit_measurement=UnitMeasurement(
                    ingredient.unit_measurement.value)
            ))
        return ingredients
