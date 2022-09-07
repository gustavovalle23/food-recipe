from enum import Enum
from typing import List
import strawberry


@strawberry.enum
class UnitMeasurement(Enum):
    MILLIGRAM = 'milligram'
    GRAM = 'gram'
    KILOGRAM = 'kilogram'
    MILLILITER = 'milliliter'
    LITER = 'liter'
    CUP = 'cup'
    TABLESPOONS = 'tablespoons'


@strawberry.type
class Ingredient:
    name: str
    quantity: float
    unit_of_measurement: UnitMeasurement


@strawberry.type
class Recipe:
    name: str
    Ingredients: List[Ingredient]
    links: List[str]
