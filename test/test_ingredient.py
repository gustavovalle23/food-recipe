import pytest

from main import schema


@pytest.mark.asyncio
async def test_should_return_avaiable_ingredients():
    query = """
        query AvaiableIngredients {
        availableIngredients{
            id
            name
            quantity
            unitMeasurement
            }
        }
    """

    result = await schema.execute(
        query
    )

    assert result.errors is None
    assert result.data.get('availableIngredients') != None
    assert len(result.data.get('availableIngredients')) > 1


@pytest.mark.asyncio
async def test_should_add_ingredient_to_recipe():
    query = """
            mutation AddIngredientToRecipe {
            addIngredientToRecipe(recipeId: "2", ingredientIds: ["1", "3"])
            }
        """

    result = await schema.execute(
        query
    )

    assert result.errors is None
    assert result.data.get('addIngredientToRecipe') == True
