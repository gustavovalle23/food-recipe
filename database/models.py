import enum
from sqlalchemy import Integer, Enum

from sqlalchemy import Column, Integer, String, Float, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship

from database.config import Base

IngredientRecipe = Table('IngredientRecipe',
                   Column('id', Integer, primary_key=True),
                   Column('ingredientId', Integer, ForeignKey('ingredients.id')),
                   Column('recipeId', Integer, ForeignKey('recipes.id')),
                   )


class UnitMeasurement(enum.Enum):
    MILLIGRAM = 'milligram'
    GRAM = 'gram'
    KILOGRAM = 'kilogram'
    MILLILITER = 'milliliter'
    LITER = 'liter'
    CUP = 'cup'
    TABLESPOONS = 'tablespoons'


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    active = Column(Boolean, default=True)


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity: Column(Float, index=True)
    unit_measurement = Column(Enum(UnitMeasurement))
    recipes = relationship('Recipe', secondary=IngredientRecipe, backref='ingredients')
    active = Column(Boolean, default=True)


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name: str
    ingredients = relationship('Ingredient', secondary=IngredientRecipe, backref='recipes')
    active = Column(Boolean, default=True)
