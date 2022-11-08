import datetime
from dog.domain.models import project
from dog.domain.models import wbs
from dog.domain.models import shared
from dog.domain.models import user
from dog.domain.models import evm


def test_evm_row_test():

    task_item = wbs.TaskItem(project.ProjectId("AAA"),wbs.TaskId("TASK001"), wbs.TaskNo("1"),
                             wbs.TaskName("設計"),wbs.TaskSchedule(shared.Term(shared.CDateTime(datetime.datetime(2022, 10, 1, 0, 0, 0, 0)), shared.CDateTime(datetime.datetime(2022, 10, 10, 0, 0, 0, 0))), shared.ManHour(10)),
                             wbs.TaskResult(shared.Term(shared.CDateTime(datetime.datetime(2022, 10, 1, 0, 0, 0, 0)), shared.CDateTime(datetime.datetime(2022, 10, 10, 0, 0, 0, 0))), shared.ManHour(10)),
                             wbs.Worker(user.UserId("TEST001"), shared.Rate(100)), shared.Rate(80))

    evm_row = evm.EvmRow(task_item)

    print(evm_row.pv)


"""コマンド実行"""
test_evm_row_test()
