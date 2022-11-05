from dataclasses import dataclass

from dog.domain.models import project, shared
from dog.domain.models import wbs


@dataclass(init=False, eq=True)
class TaskItem:
    project_id: project.ProjectId
    task_id: wbs.TaskId
    task_no: wbs.TaskNo
    task_name: wbs.TaskName
    task_schedule: wbs.TaskSchedule
    task_result: wbs.TaskResult
    task_assign: wbs.Worker
    task_progress_rate: shared.Rate

    def __init__(self,
                 project_id: project.ProjectId,
                 task_id: wbs.TaskId,
                 task_no: wbs.TaskNo,
                 task_name: wbs.TaskName,
                 task_schedule: wbs.TaskSchedule,
                 task_result: wbs.TaskResult,
                 task_assign: wbs.Worker,
                 task_progress_rate: shared.Rate):
        self.project_id = project_id
        self.task_id = task_id
        self.task_no = task_no
        self.task_name = task_name
        self.task_schedule = task_schedule
        self.task_result = task_result
        self.task_assign = task_assign
        self.task_progress_rate = task_progress_rate
