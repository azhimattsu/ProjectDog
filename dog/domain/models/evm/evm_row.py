from dataclasses import dataclass
import datetime

from dog.domain.models import shared
from dog.domain.models import wbs
from dog.domain.models.shared.cdatetime import CDateTime
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
        self.pv = get_terms(task_item.task_schedule.term.start_day, task_item.task_schedule.term.end_day, CDateTime(datetime.datetime.now()))


def get_terms(start: CDateTime, end: CDateTime, ref: CDateTime) -> int:

    ''' 開始日 < 参照日の場合は0日'''
    if ref.value < start.value:
        return 0

    ''' 参照日 < 終了日の場合は0日'''
    if ref.value < end.value:
        return (ref - start).days + 1

    ''' 終了日 - 開始日'''
    return (end - start).days + 1
