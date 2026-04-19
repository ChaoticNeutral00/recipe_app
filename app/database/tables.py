from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

Base = declarative_base()

class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    serving_size: Mapped[float] = mapped_column()
    serving_units: Mapped[str] = mapped_column()
    cal: Mapped[int] = mapped_column()
    protein: Mapped[int] = mapped_column()
    fat: Mapped[int] = mapped_column()
    carbs: Mapped[int] = mapped_column()

    recipe_ingredients: Mapped[list["RecipeIngredient"]] = relationship(back_populates="ingredient")

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id"), nullable=False)
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredients.id"), nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    units: Mapped[str] = mapped_column(nullable=False)

    recipe: Mapped["Recipe"] = relationship(back_populates="recipe_ingredients")
    ingredient: Mapped["Ingredient"] = relationship(back_populates="recipe_ingredients")

class RecipeStep(Base):
    __tablename__ = "recipe_steps"

    id: Mapped[int] = mapped_column(primary_key=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id"), nullable=False)
    step_num: Mapped[int] = mapped_column(nullable=False)
    instruction: Mapped[str] = mapped_column(nullable=False)

    recipe: Mapped["Recipe"] = relationship(back_populates="steps")

class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    recipe_ingredients: Mapped[list["RecipeIngredient"]] = relationship(back_populates="recipe")
    steps: Mapped[list["RecipeStep"]] = relationship(back_populates="recipe")

