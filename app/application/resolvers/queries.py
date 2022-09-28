import strawberry
from typing import List
from kink import di

from app.domain.usecases.recipe import FindAllRecipesUseCase,FindRecipesWithIngredientsUseCase
from app.domain.usecases.ingredient import FindAllIngredientsUseCase
from app.infra.shared.builders import IngredientBuilder, RecipeBuilder
from app.application.graphql_types.recipe import Ingredient, Recipe


@strawberry.type
class Query:

    @strawberry.field
    async def available_recipes(self) -> List[Recipe]:
        print('Request to availableRecipes')
        use_case: FindAllRecipesUseCase = di[FindAllRecipesUseCase]
        recipes_db = await use_case.perform()
        return RecipeBuilder.build_list(recipes_db)

    @strawberry.field
    async def available_ingredients(self) -> List[Ingredient]:
        print('Request to availableIngredients')
        use_case: FindAllIngredientsUseCase = di[FindAllIngredientsUseCase]
        ingredients_db = await use_case.perform()
        return IngredientBuilder.build_list(ingredients_db)

    @strawberry.field
    async def recipes_with_ingredients(self, ingredient_ids: List[int]) -> List[Recipe]:
        print(f'Request to recipesWithIngredients: {ingredient_ids}')
        use_case: FindRecipesWithIngredientsUseCase = di[FindRecipesWithIngredientsUseCase]
        recipes_db = await use_case.perform(ingredient_ids)
        return RecipeBuilder.build_list(recipes_db)
