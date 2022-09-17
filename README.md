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
mutation {
  createIngredient(ingredient: {
    name: "Marshmellow",
    quantity: 1,
    unitMeasurement: GRAM
  })
}
```

# To export GraphQL schema:
strawberry export-schema main:schema > schema.graphql
