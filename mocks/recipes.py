from graphql_types.recipe import Ingredient, Recipe, UnitMeasurement


def get_all_recipes():
    return [
        Recipe(
            name='Key Lime Pie',
            links=['https://www.allrecipes.com/recipe/12224/key-lime-pie-i/',
                   'https://www.onceuponachef.com/recipes/key-lime-pie.html'],
            Ingredients=[
                Ingredient(
                    name='Graham cracker crumbs',
                    quantity=1,
                    unit_of_measurement=UnitMeasurement.CUP
                ),
                Ingredient(
                    name='White sugar',
                    quantity=3,
                    unit_of_measurement=UnitMeasurement.TABLESPOONS
                )
            ]
        ),
    ]
