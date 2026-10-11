"""Price helpers. Amounts are integer cents."""

from __future__ import annotations


def apply_discount(cents: int, percent: int) -> int:
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(cents * (100 - percent) / 100)


def cart_total(lines: list[tuple[int, int]], discount_percent: int = 0) -> int:
    """Sum (unit_cents, quantity) lines, then apply a cart-wide discount."""
    subtotal = sum(unit * qty for unit, qty in lines)
    return apply_discount(subtotal, discount_percent)
