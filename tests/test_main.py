import pytest

from app.main import sestej, odstej, pomnozi, deli


def test_sestej():
    assert sestej(2, 3) == 5


def test_odstej():
    assert odstej(10, 4) == 6


def test_pomnozi():
    assert pomnozi(3, 4) == 12


def test_deli():
    assert deli(10, 2) == 5


def test_deli_z_nic():
    with pytest.raises(ValueError):
        deli(10, 0)

