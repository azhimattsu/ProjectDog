from dataclasses import dataclass

from dog.domain.models import shared


@dataclass(init=False, eq=True)
class Term():
    start_day: shared.CDateTime
    end_day: shared.CDateTime

    def __init__(self,
                 start_day: shared.CDateTime,
                 end_day: shared.CDateTime):
        self.start_day = start_day
        self.end_day = end_day
