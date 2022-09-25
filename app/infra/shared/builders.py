from typing import List

from app.application.graphql_types.recipe import (Ingredient, Recipe,
                                                  UnitMeasurement)
from app.infra.models import Ingredient as SchemaIngredient
from app.infra.models import Recipe as SchemaRecipe


class IngredientBuilder:
    @staticmethod
    def build_one(ingredient: SchemaIngredient) -> Ingredient:
        return Ingredient(
            id=ingredient.id,
            name=ingredient.name,
            quantity=ingredient.quantity,
            unit_measurement=UnitMeasurement(ingredient.unit_measurement.value)
        )

    @staticmethod
    def build_list(ingredients_db: List[SchemaIngredient]) -> List[Ingredient]:
        return map(IngredientBuilder.build_one, ingredients_db)


class RecipeBuilder:
    @staticmethod
    def build_one(recipe: SchemaRecipe) -> Recipe:
        return Recipe(
            id=recipe.id,
            name=recipe.name,
            ingredients=IngredientBuilder.build_list(recipe.ingredients),
            link=recipe.link
        )

    @staticmethod
    def build_list(recipes_db: List[SchemaRecipe]) -> List[Recipe]:
        return map(RecipeBuilder.build_one, recipes_db)
