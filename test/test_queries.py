import pytest

from main import schema


@pytest.mark.asyncio
async def test_query():
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
