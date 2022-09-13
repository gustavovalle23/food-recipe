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
        return [
            Ingredient(
                name=ingredient.name,
                quantity=ingredient.quantity,
                unit_measurement=UnitMeasurement(
                    ingredient.unit_measurement.value)
            ) for ingredient in ingredients_db
        ]


class RecipeBuilder:
    @staticmethod
    def build_one(recipe: SchemaRecipe) -> Recipe:
        return Recipe(
            name=recipe.name,
            # Ingredients=IngredientBuilder.buid_list(recipe.ingredients),
            link=recipe.link
        )

    @staticmethod
    def build_list(recipes_db: List[SchemaRecipe]) -> List[Recipe]:
        ...
