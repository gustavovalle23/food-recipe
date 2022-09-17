# Avaiable queries:

```graphql
query RecipesWithIngredients {
  recipesWithIngredients (ingredientIds: [1, 4, 5]) {
    id
    name
    Ingredients {
      id
      name
      quantity
      unitMeasurement
    }
    link
  }
}

query AvaiableIngredients {
  availableIngredients{
    id
    name
    quantity
    unitMeasurement
  }
}


query AvailableRecipes {
  availableRecipes {
    id
    name
    link
	Ingredients {
      id
      name
      quantity
      unitMeasurement
    }
  }
}
```

# Avaiable mutations:
```graphql
mutation CreateIngredient {
  createIngredient(ingredient: {
    name: "Marshmellow",
    quantity: 1,
    unitMeasurement: GRAM
  })
}

mutation CreateRecipe {
  createRecipe(recipe: {
    name: "Orange Pie",
    link: "https://www.recipelink.com/recipecards/889_dinner_with_peaches.html"
  })
}

mutation AddIngredientToRecipe {
  addIngredientToRecipe(recipeId: "1", ingredientIds: ["1", "3"])
}

```

# To export GraphQL schema:
strawberry export-schema main:schema > schema.graphql


### recipesWithIngredients used following sql query
```sql
SELECT *
FROM recipes r
WHERE r.id NOT IN (
	SELECT recipe_id
	FROM ingredient_recipe
	WHERE ingredient_id NOT IN (10, 2, 4, 5, 1)
)
AND r.id IN (
	SELECT ir.recipe_id
	FROM ingredient_recipe ir
)
```