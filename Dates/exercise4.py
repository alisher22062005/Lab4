import datetime

today_day=datetime.datetime.now()
some_day=datetime.datetime(2024,12,8)
if today_day>some_day:
    difference=today_day-some_day
else:
    difference=some_day-today_day

print (difference.total_seconds())


