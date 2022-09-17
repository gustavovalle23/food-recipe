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
