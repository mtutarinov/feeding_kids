import pytest

from cart.dish_constructor import DishConstructor
from tests.factories import (
    AllergenFactory,
    ChildFactory,
    DishFactory,
    IngredientFactory,
)

# DISH_CONSTRUCTOR_URL ='/api/v1/dish_constructor/'


@pytest.mark.django_db
def test_dish_constructor():
    ingredient_a = IngredientFactory.create()
    ingredient_b = IngredientFactory.create()
    ingredient_c = IngredientFactory.create()
    ingredient_d = IngredientFactory.create()
    ingredient_e = IngredientFactory.create()
    available_ids = [
        ingredient_a.id,
        ingredient_b.id,
        ingredient_c.id,
        ingredient_d.id,
        ingredient_e.id,
    ]
    dish_a = DishFactory.create(ingredients=(ingredient_a,))
    dish_b = DishFactory.create(ingredients=(ingredient_a, ingredient_b))
    dish_c = DishFactory.create(ingredients=(ingredient_a, ingredient_b, ingredient_c))
    dish_d = DishFactory.create(
        ingredients=(ingredient_a, ingredient_b, ingredient_c, ingredient_d)
    )
    dish_e = DishFactory.create(
        ingredients=(
            ingredient_a,
            ingredient_b,
            ingredient_c,
            ingredient_d,
            ingredient_e,
        )
    )
    child = ChildFactory.create()
    allergen_a = AllergenFactory.create(child=child, ingredient=ingredient_a)
    allergen_b = AllergenFactory.create(child=child, ingredient=ingredient_b)
    allergen_c = AllergenFactory.create(child=child, ingredient=ingredient_c)
    allergen_ids = [allergen_a.id, allergen_b.id, allergen_c.id]
    result = DishConstructor.get(available_ids, allergen_ids)
    assert len(result) == 5
    assert result[0] == dish_a
    assert result[1] == dish_b
    assert result[2] == dish_d
    assert result[3] == dish_c
    assert result[4] == dish_e
