import datetime

today_day=datetime.datetime.now()
some_day=datetime.datetime(2024,1,18)

if today_day>some_day:
    difference=today_day-some_day

elif today_day==some_day:
    difference=0

else:
    difference=some_day-today_day

print (difference.total_seconds())


