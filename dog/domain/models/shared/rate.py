from dataclasses import dataclass


@dataclass(init=False, eq=True)
class Rate:
    value: int = 0

    def __init__(self, value: int):
        self.value = value
