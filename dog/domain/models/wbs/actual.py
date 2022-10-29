from dataclasses import dataclass

from dog.domain.models import shared
from dog.domain.models import wbs


@dataclass(init=False, eq=True)
class Actual():
    task_id: wbs.TaskId
    start_day: shared.CDateTime
    end_day: shared.CDateTime

    def __init__(self,
                 task_id: wbs.TaskId,
                 start_day: shared.CDateTime,
                 end_day: shared.CDateTime):
        self.task_id = task_id
        self.end_day = end_day
