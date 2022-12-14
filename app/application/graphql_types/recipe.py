from datetime import datetime
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
    id: str
    name: str
    quantity: float
    unit_measurement: UnitMeasurement


@strawberry.type
class Recipe:
    id: str
    name: str
    ingredients: List[Ingredient]
    link: str


@strawberry.type
class User:
    id: str
    username: str
    birth_date: datetime
