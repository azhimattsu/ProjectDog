from dataclasses import dataclass


@dataclass(init=False, eq=True)
class TaskName:
    value: str = ""

    def __init__(self, value: str):
        self.value = value
