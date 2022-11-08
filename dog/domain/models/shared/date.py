from datetime import datetime, timedelta


class CDate:
    value: datetime.date

    def __init__(self, value: datetime.date):
        self.value = value

    def __sub__(self, other) -> timedelta:
        return other.value - self.value


def new_date_from_str(value: str) -> CDate:
    return datetime.strptime(value, "%Y-%m-%d").date()
