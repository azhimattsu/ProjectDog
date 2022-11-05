from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from dog.infrastructure.mysql.mysql_setting import Base

from dog.domain.models import shared
from dog.domain.models import wbs


class TaskScheduleDataModel(Base):
    __tablename__ = "task_schedule"
    task_id = Column(String(64), primary_key=True, nullable=False)
    start_day = Column(DateTime, default=datetime.utcnow)
    end_day = Column(DateTime, default=datetime.utcnow)
    work_man_hour = Column(Integer, nullable=False)

    def import_entity(self, id: wbs.TaskId, entity: wbs.TaskSchedule):
        self.task_id = id.value
        self.start_day = entity.term.start_day.value
        self.end_day = entity.term.end_day.value
        self.work_man_hour = entity.work_man_hour.value


def from_entity(id: wbs.TaskId, entity: wbs.TaskSchedule) -> TaskScheduleDataModel:
    target = TaskScheduleDataModel()
    target.import_entity(id, entity)
    return target


def to_entity(row: TaskScheduleDataModel) -> wbs.TaskSchedule:
    target = wbs.TaskSchedule(shared.CDateTime(row.start_day),
                              shared.CDateTime(row.end_day),
                              shared.ManHour(row.work_man_hour))

    return target
