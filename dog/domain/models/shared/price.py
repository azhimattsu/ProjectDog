from dataclasses import dataclass


@dataclass(init=False, eq=True)
class Price:
    value: int = 0

    def __init__(self, value: int):
        self.value = value
