import pytest

from shelf import paginate

ITEMS = list(range(1, 26))  # 25 items


def test_first_page():
    p = paginate(ITEMS, page=1, per_page=10)
    assert p.items == list(range(1, 11))
    assert p.has_next


def test_second_page():
    p = paginate(ITEMS, page=2, per_page=10)
    assert p.items == list(range(11, 21))


def test_last_page_is_partial():
    p = paginate(ITEMS, page=3, per_page=10)
    assert p.items == [21, 22, 23, 24, 25]
    assert p.pages == 3
    assert not p.has_next


def test_page_past_end_is_empty():
    assert paginate(ITEMS, page=4, per_page=10).items == []


@pytest.mark.parametrize("page,per_page", [(0, 10), (1, 0)])
def test_invalid_arguments(page, per_page):
    with pytest.raises(ValueError):
        paginate(ITEMS, page=page, per_page=per_page)
