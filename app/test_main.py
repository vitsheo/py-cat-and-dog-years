import app.main


def test_zero_years() -> None:
    """Перевірка для нульового віку тварин."""
    assert app.main.get_human_age(0, 0) == [0, 0]


def test_before_first_human_year_boundary() -> None:
    """Перевірка значень безпосередньо перед досягненням

    1 людського року (14 років).
    """
    assert app.main.get_human_age(14, 14) == [0, 0]


def test_exactly_first_human_year() -> None:
    """Перевірка досягнення першої межі (рівно 15 років)."""
    assert app.main.get_human_age(15, 15) == [1, 1]


def test_before_second_human_year_boundary() -> None:
    """Перевірка значень перед досягненням 2 людських років

    (15 + 8 = 23 роки).
    """
    assert app.main.get_human_age(23, 23) == [1, 1]


def test_exactly_second_human_year() -> None:
    """Перевірка досягнення другої межі (15 + 9 = 24 роки)."""
    assert app.main.get_human_age(24, 24) == [2, 2]


def test_subsequent_years_boundaries() -> None:
    """Перевірка накопичення наступних років, коли кроки

    для котів (4) та собак (5) різняться.
    """
    assert app.main.get_human_age(27, 27) == [2, 2]
    assert app.main.get_human_age(28, 28) == [3, 2]
    assert app.main.get_human_age(28, 29) == [3, 3]


def test_large_values() -> None:
    """Перевірка обчислення великих значень віку."""
    assert app.main.get_human_age(100, 100) == [21, 17]


def test_independent_aging() -> None:
    """Перевірка, що вік кота і собаки обчислюється

    незалежно один від одного.
    """
    assert app.main.get_human_age(15, 28) == [1, 2]
    assert app.main.get_human_age(28, 15) == [3, 1]
