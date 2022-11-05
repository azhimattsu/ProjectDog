from dataclasses import dataclass

from dog.domain.models import shared
from dog.domain.models import wbs
from dog.domain.models.shared.decimal_value import DecimalValue


@dataclass(init=False, eq=True)
class EvmRow():
    pv: DecimalValue
    ev: DecimalValue
    sv: DecimalValue
    cv: DecimalValue
    cpi: DecimalValue
    spi: DecimalValue
    work_man_hour: shared.ManHour

    def __init__(self,
                 task_item: wbs.TaskItem):
        self.pv = task_item.task_schedule.work_man_hour
