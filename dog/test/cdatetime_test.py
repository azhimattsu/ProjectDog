import datetime
from dog.domain.models import shared
from dog.domain.models.shared.date import new_date_from_str


def cdatetime_test():

    dt1 = shared.CDateTime(datetime.datetime.now())
    print(dt1.value)

    dt2 = shared.CDateTime(datetime.datetime(2022, 11, 20, 0, 0, 0, 0))
    print(dt2.value)

    print((dt2 - dt1).days)

    dt3 = shared.new_datetime_from_str("2022-12-01 01:12:23")
    print(dt3.value)


def cdate_test():
    day1 = new_date_from_str("2022-11-01")
    print(day1)

    day2 = new_date_from_str("2022-11-05")
    print(day2)

    print((day2 - day1).days)


"""コマンド実行"""
cdate_test()
cdatetime_test()
