"""1-based pagination over a sequence."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Generic, Sequence, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Page(Generic[T]):
    items: list[T]
    page: int
    per_page: int
    total: int

    @property
    def pages(self) -> int:
        return max(1, math.ceil(self.total / self.per_page))

    @property
    def has_next(self) -> bool:
        return self.page < self.pages


def paginate(items: Sequence[T], page: int = 1, per_page: int = 10) -> Page[T]:
    """Return page ``page`` (1-based) of ``items`` with ``per_page`` entries per page."""
    if page < 1:
        raise ValueError("page must be >= 1")
    if per_page < 1:
        raise ValueError("per_page must be >= 1")
    start = (page - 1) * per_page
    end = start + per_page
    return Page(items=list(items[start:end]), page=page, per_page=per_page, total=len(items))
