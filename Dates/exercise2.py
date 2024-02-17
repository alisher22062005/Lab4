import datetime

today_day=datetime.datetime.now()
tomorrow_day=today_day+datetime.timedelta(days=1)
yestarday_day=today_day-datetime.timedelta(days=1)
print(today_day)
print(tomorrow_day)
print(yestarday_day)