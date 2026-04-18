from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

Base = declarative_base()

class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    serving_size: Mapped[str] = mapped_column()
    serving_units: Mapped[str] = mapped_column()
    cal: Mapped[int] = mapped_column()
    protein: Mapped[int] = mapped_column()
    fat: Mapped[int] = mapped_column()
    carbs: Mapped[int] = mapped_column()

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    recipe_id: Mapped[int] = relationship(back_populates="recipes", nullable=False)
    ingredient_id: Mapped[int] = relationship(back_populates="ingredients", nullable=False)
    amount: Mapped[str] = mapped_column(nullable=False)
    units: Mapped[str] = mapped_column(nullable=False)

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

