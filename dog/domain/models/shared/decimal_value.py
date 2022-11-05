from dataclasses import dataclass
from decimal import ROUND_UP, Decimal


@dataclass(init=False, eq=True)
class DecimalValue:
    value: Decimal = 0

    def __init__(self, value: Decimal):
        self.value = value.quantize(Decimal(".01"), rounding=ROUND_UP)
