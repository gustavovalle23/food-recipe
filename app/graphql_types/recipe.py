import enum
from typing import List
import strawberry


@strawberry.enum
class UnitMeasurement(enum.Enum):
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
    unit_measurement: UnitMeasurement


@strawberry.type
class Recipe:
    name: str
    Ingredients: List[Ingredient]
    link: str
