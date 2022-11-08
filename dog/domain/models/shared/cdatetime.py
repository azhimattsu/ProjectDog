from datetime import datetime, timedelta


class CDateTime:
    value: datetime

    def __init__(self, value: datetime):
        self.value = value

    def __sub__(self, other) -> timedelta:
        return self.value - other.value

    def getStr(self) -> str:
        return self.value.strftime("%Y-%m-%d %H:%M:%S")


def new_datetime_from_str(value: str) -> CDateTime:
    """
    文字列からCDateTimeを生成する。
    書式：'2017-05-23 12:47:23'
    """
    return CDateTime(datetime.strptime(value, "%Y-%m-%d %H:%M:%S"))
