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
async def test_should_return_avaiable_recipes():
    query = """
        query AvailableRecipes {
            availableRecipes {
                id
                name
                link
                ingredients {
                id
                name
                quantity
                unitMeasurement
                }
            }
        }
    """

    result = await schema.execute(
        query
    )

    assert result.errors is None
    assert result.data.get('availableRecipes') != None
    assert result.data.get('availableRecipes')[0].get('name') == 'Pie'


@pytest.mark.asyncio
async def test_should_return_recipes_with_ingredients():
    query = """
        query RecipesWithIngredients {
            recipesWithIngredients (ingredientIds: [1,2,4]) {
                id
                name
                ingredients {
                id
                name
                quantity
                unitMeasurement
                }
                link
            }
        }
        """

    result = await schema.execute(
        query
    )

    assert result.errors is None
    assert result.data.get('recipesWithIngredients') != None
    assert result.data.get('recipesWithIngredients')[0].get('name') == 'Pie'
