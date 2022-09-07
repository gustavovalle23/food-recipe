import typing
from schemas.dtos.recipe import IngredientDto
from schemas.recipe import Ingredient, Recipe, UnitMeasurement


def recipes_with_ingredients_use_case(ingredients: typing.List[IngredientDto]):
	return Recipe(name='222', Ingredients=[Ingredient(name='221', quantity=1, unit_of_measurement=UnitMeasurement.CUP)], links=[])
