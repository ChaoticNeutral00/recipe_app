# Performs CRUD operations with the database
from sqlalchemy import insert

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

stmt = insert(ingredients).values(name="onion", serving_size=1.0)
print(stmt)