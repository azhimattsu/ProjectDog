from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from dog.infrastructure.mysql.mysql_setting import Base

from dog.domain.models import project, shared, user
from dog.domain.models import wbs


class TaskItemDataModel(Base):
    __tablename__ = "task_item"
    project_id = Column(String(64), primary_key=True, nullable=False)
    task_id = Column(String(64), primary_key=True, nullable=False)
    task_no = Column(String(10), nullable=False)
    task_name = Column(String(100), nullable=False)
    task_assign = Column(String(64), nullable=False)
    task_progress_rate = Column(Integer, nullable=False)

    def import_entity(self, entity: wbs.TaskItem):
        self.project_id = entity.project_id.value
        self.task_id = entity.task_id.value
        self.task_no = entity.task_no.value
        self.task_name = entity.task_name.value
        self.task_assign = entity.task_assign.user_id.value
        self.task_progress_rate = entity.task_progress_rate.value


def from_entity(entity: wbs.TaskItem) -> TaskItemDataModel:
    target = TaskItemDataModel()
    target.import_entity(entity)
    return target


def to_entity(row: TaskItemDataModel) -> wbs.TaskItem:
    target = wbs.TaskItem(project.ProjectId(row.project_id),
                          wbs.TaskId(row.task_id),
                          wbs.TaskNo(row.task_no),
                          wbs.TaskName(row.task_name),
                          wbs.Worker(user.UserId(row.task_assign), user.UserName("")),
                          shared.Rate(row.task_progress_rate))

    return target
