import datetime

today_day=datetime.datetime.now()
x=str(today_day)
without_sec=""
for i in x:
    if i==".":
        break
    without_sec+=i
print(today_day)
print(without_sec)