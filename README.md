# Avaiable queries:

```graphql
query {
  availableRecipes {
    name
    Ingredients {
      name
      quantity
      unitOfMeasurement
    }
    links
  }
}

query{
  recipesWithIngredients(ingredients: [1, 2, 23, 64]) {
    name
    Ingredients {
      name
      quantity
      unitOfMeasurement
    }
    links
  }
}

query {
  availableIngredients {
    name
    quantity
    unitOfMeasurement
  }
}
```

# To export GraphQL schema:
strawberry export-schema main:schema > schema.graphql
