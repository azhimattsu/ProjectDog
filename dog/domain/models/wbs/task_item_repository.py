from abc import ABCMeta
from abc import abstractclassmethod

from dog.domain.models import project
from dog.domain.models import wbs


class TaskItemRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def find_data_byprojectid(self, id: project.ProjectId) -> list[wbs.TaskItem]:
        pass

    @abstractclassmethod
    def create_data(self, task_item: wbs.TaskItem):
        pass

    @abstractclassmethod
    def update_data(self, task_item: wbs.TaskItem):
        pass
