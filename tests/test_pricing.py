import pytest

from shelf import apply_discount, cart_total


def test_apply_discount():
    assert apply_discount(1000, 15) == 850


def test_cart_total_with_discount():
    assert cart_total([(250, 2), (1000, 1)], discount_percent=10) == 1350


def test_discount_out_of_range():
    with pytest.raises(ValueError):
        apply_discount(1000, 120)
