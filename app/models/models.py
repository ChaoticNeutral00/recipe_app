from dataclasses import dataclass, field

@dataclass
class Ingredient:
    name: str = ""
    serving_size: float = 0.0
    serving_units: str = ""
    cal: int = 0
    protein: int = 0
    fat: int = 0
    carbs: int = 0

@dataclass
class RecipeIngredient:
    ingredient: Ingredient | None = None
    amount: float = 0.0
    units: str = ""

@dataclass
class Recipe:
    name: str = ""
    ingredients: list[RecipeIngredient] = field(default_factory=list)
    directions: list[str] = field(default_factory=list)