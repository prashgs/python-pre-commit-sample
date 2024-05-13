from __future__ import annotations


def add_numbers(x: int, y: int) -> int | None:
    if x:
        return x + y
    return None


class TestOne:

    def __init__(self, id_test: int) -> None:
        self.id_test = id_test
