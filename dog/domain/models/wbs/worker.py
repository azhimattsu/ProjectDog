from dataclasses import dataclass

from dog.domain.models import shared
from dog.domain.models import user


@dataclass(init=False, eq=True)
class Worker():
    user_id: user.UserId
    work_rate: shared.Rate

    def __init__(self,
                 user_id: user.UserId,
                 work_rate: shared.Rate):
        self.user_id = user_id
        self.work_rate = work_rate
