import enum

import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy import (
    Enum, Column, Integer, String, Date,
    Float, Boolean, Table, ForeignKey,
    insert
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

IngredientRecipe = Table('ingredient_recipe',
                         Base.metadata,
                         Column('ingredient_id', ForeignKey(
                             'ingredients.id'), primary_key=True),
                         Column('recipe_id', ForeignKey(
                             'recipes.id'), primary_key=True),
                         )


class UnitMeasurement(enum.Enum):
    MILLIGRAM = 'milligram'
    GRAM = 'gram'
    KILOGRAM = 'kilogram'
    MILLILITER = 'milliliter'
    LITER = 'liter'
    CUP = 'cup'
    TABLESPOONS = 'tablespoons'


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    quantity = Column(Float, index=True)
    unit_measurement = Column(Enum(UnitMeasurement))
    recipes = relationship(
        'Recipe', secondary=IngredientRecipe, back_populates='ingredients')
    active = Column(Boolean, default=True)


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = relationship(
        'Ingredient', secondary=IngredientRecipe, back_populates='recipes')
    active = Column(Boolean, default=True)
    link = Column(String, index=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.name}'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String, index=True)
    birth_date = Column(Date, index=True)
    active = Column(Boolean, default=True)


engine = create_async_engine(
    "sqlite+aiosqlite:///./database.db", connect_args={"check_same_thread": False}
)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
            finally:
                await session.close()


async def seeds():
    async with get_session() as session:
        sql = insert(Recipe).values(
            name='Pie',
            active=True,
            link='https://www.tasteofhome.com/recipes/world-s-best-lemon-pie')
        await session.execute(sql)

        sql = insert(Recipe).values(
            name='Easy pancakes',
            active=True,
            link='https://www.bbcgoodfood.com/recipes/easy-pancakes')
        await session.execute(sql)

        sql = insert(Recipe).values(
            name='Chilli con carne',
            active=True,
            link='https://www.bbcgoodfood.com/recipes/chilli-con-carne-recipe')
        await session.execute(sql)

        sql = insert(Recipe).values(
            name='Yummy golden syrup flapjacks',
            active=True,
            link='https://www.bbcgoodfood.com/recipes/yummy-golden-syrup-flapjacks')
        await session.execute(sql)

        sql = insert(Ingredient).values(
            name='Strawberry',
            quantity=10,
            unit_measurement=UnitMeasurement.GRAM,
        )
        await session.execute(sql)

        sql = insert(Ingredient).values(
            name='Lemon',
            quantity=5,
            unit_measurement=UnitMeasurement.CUP,
        )
        await session.execute(sql)

        sql = insert(Ingredient).values(
            name='Apple',
            quantity=2,
            unit_measurement=UnitMeasurement.GRAM,
        )
        await session.execute(sql)

        sql = insert(Ingredient).values(
            name='Sugar',
            quantity=10,
            unit_measurement=UnitMeasurement.TABLESPOONS,
        )
        await session.execute(sql)

        sql = insert(IngredientRecipe).values(
            recipe_id=1,
            ingredient_id=1
        )
        await session.execute(sql)

        sql = insert(IngredientRecipe).values(
            recipe_id=1,
            ingredient_id=2
        )
        await session.execute(sql)

        sql = insert(IngredientRecipe).values(
            recipe_id=2,
            ingredient_id=3
        )
        await session.execute(sql)

        sql = insert(IngredientRecipe).values(
            recipe_id=1,
            ingredient_id=4
        )
        await session.execute(sql)

        await session.commit()


async def _async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
    await seeds()


if __name__ == "__main__":
    print("Dropping and creating tables")
    asyncio.run(_async_main())
    print("Done.")
