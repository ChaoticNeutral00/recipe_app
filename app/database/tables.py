from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey

Base = declarative_base()

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False)
    serving_size = Column("serving_size", Float)
    serving_units = Column("serving_units", String)
    cal = Column("calories", Integer)
    protein = Column("protein", Integer)
    fat = Column("fat", Integer)
    carbs = Column("carbs", Integer)

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id = Column("id", Integer, primary_key=True)
    recipe_id = Column("recipe_id", Integer, ForeignKey("recipes.id"), nullable=False)
    ingredient_id = Column("ingredient_id", Integer, ForeignKey("ingredients.id"), nullable=False)
    amount = Column("amount", Float, nullable=False)
    units = Column("units", String, nullable=False)

class RecipeStep(Base):
    __tablename__ = "recipe_steps"

    id = Column("id", Integer, primary_key=True)
    recipe_id = Column("recipe_id", Integer, ForeignKey("recipes.id"), nullable=False)
    step_num = Column("step_number", Integer, nullable=False)
    instruction = Column("instruction", String, nullable=False)

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False)

