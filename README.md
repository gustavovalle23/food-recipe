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
  recipesWithIngredients(ingredients: [
    {
    name: "Ingredient 1",
    quantity: 1
    },
    {
    name: "Ingredient 2",
    quantity: 5
    }
  ]) {
    name
    Ingredients {
      name
      quantity
      unitOfMeasurement
    }
    links
  }
}
```
