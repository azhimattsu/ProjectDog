from abc import ABCMeta
from abc import abstractclassmethod
from typing import Optional

from dog.domain.models import wbs


class TaskScheduleRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def find_data_byid(self, id: wbs.TaskId) -> Optional[wbs.TaskSchedule]:
        pass

    @abstractclassmethod
    def create_data(self, id: wbs.TaskId, task_schedule: wbs.TaskSchedule):
        pass

    @abstractclassmethod
    def update_data(self, id: wbs.TaskId, task_schedule: wbs.TaskSchedule):
        pass
