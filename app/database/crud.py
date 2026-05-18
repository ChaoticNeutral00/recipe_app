# Performs CRUD operations with the database
# python libraries
from sqlalchemy import select

# Application libraries
from app.database.engine import get_session_factory
from app.database.tables import Ingredient, RecipeIngredient, Recipe, RecipeStep


Session = get_session_factory(testing=True)

### FLow
# Create Recipe
#     ↓
# Recipe exists in DB with an id
#     ↓
# Look up existing Ingredient
#     ↓
# Create RecipeIngredient linking:
#     recipe_id + ingredient_id + amount + units

def get_all_ingredients():
      with Session() as session:
            statement = select(Ingredient)

            rows = session.execute(statement).scalars().all()

            for row in rows:
                  print(row)
      

def add_ingredient(name: str, serving_size: float, serving_units: str, cal: int, protein: int, fat: int, carbs: int):
      with Session() as session:
            ingredient = Ingredient(
                name=name,
                serving_size=serving_size,
                serving_units=serving_units,
                cal=cal,
                protein=protein,
                fat=fat,
                carbs=carbs,
                )
            session.add(ingredient)
            session.commit()

            return ingredient
            
def add_recipeIngredient(ingredient: Ingredient, amount: float, units: str):
      with Session() as session:
            recipeIngredient = RecipeIngredient(
                  ingredient=ingredient,
                  amount=amount,
                  units=units
            )
            session.add(recipeIngredient)
            session.commit()

            return recipeIngredient

# I want to create function that inserts an ingredient into the database
# so well need to connect to the database and perform that insert opeartion.


# @dataclass
# class RecipeIngredient:
#     ingredient: Ingredient | None = None
#     amount: float = 0.0
#     units: str = ""

# class Ingredient(Base):
#     __tablename__ = "ingredients"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(nullable=False)
#     serving_size: Mapped[float] = mapped_column()
#     serving_units: Mapped[str] = mapped_column()
#     cal: Mapped[int] = mapped_column()
#     protein: Mapped[int] = mapped_column()
#     fat: Mapped[int] = mapped_column()
#     carbs: Mapped[int] = mapped_column()

#     recipe_ingredients: Mapped[list["RecipeIngredient"]] = relationship(back_populates="ingredient")

# add_ingredient("test", 3.5,"oz", 20, 1,3,5)
get_all_ingredients()