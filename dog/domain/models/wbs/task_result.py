from dataclasses import dataclass

from dog.domain.models import shared


@dataclass(init=False, eq=True)
class TaskResult():
    term: shared.Term
    work_man_hour: shared.ManHour

    def __init__(self,
                 term: shared.Term,
                 work_man_hour: shared.ManHour):
        self.term = term
        self.work_man_hour = work_man_hour
