import datetime

currentDatetime = datetime.datetime.now()
DDatetime=datetime.datetime(2024, 2, 10)
deltatime=currentDatetime-DDatetime
print(deltatime.total_seconds())
