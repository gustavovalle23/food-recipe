import enum
from sqlalchemy import Integer, Enum

from sqlalchemy import Column, Integer, String, Float, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship

import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator

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


async def _async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()


if __name__ == "__main__":
    print("Dropping and creating tables")
    asyncio.run(_async_main())
    print("Done.")
