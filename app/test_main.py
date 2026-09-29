import pytest
import app.main


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        # Граничні значення до 1 року (до 15 років)
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        # Межа 1 людського року (рівно 15 років)
        (15, 15, [1, 1]),
        # Граничні значення до 2 років (від 15 до 23 років)
        (23, 23, [1, 1]),
        # Межа 2 людських років (рівно 24 роки)
        (24, 24, [2, 2]),
        # Наступні роки, де кроки різняться (кіт: 4 роки, собака: 5 років)
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        # Великі значення
        (100, 100, [21, 17]),
    ]
)
def test_human_age_boundaries(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    """Перевірка граничних значень віку котів та собак за PEP 8."""
    assert app.main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (15, 28, [1, 2]),
        (28, 15, [3, 1]),
    ]
)
def test_independent_aging(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    """Перевірка незалежного обчислення віку для кота і собаки."""
    assert app.main.get_human_age(cat_age, dog_age) == expected
