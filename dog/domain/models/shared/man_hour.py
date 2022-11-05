from dataclasses import dataclass


@dataclass(init=False, eq=True)
class ManHour:
    value: float = 0

    def __init__(self, value: float):
        self.value = value
