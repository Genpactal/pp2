import datetime

currentDatetime = datetime.datetime.now()

currentDatetimeWithoutMicroseconds = currentDatetime.replace(microsecond=0)

print("Datetime without microseconds:", currentDatetimeWithoutMicroseconds)
