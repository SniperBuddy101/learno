# Working with datetime objects and timedeltas

from datetime import datetime, timedelta
from time import time

dt_obj = datetime(2020, 4, 7) + timedelta(days=5, seconds=200, microseconds=96)
dt_obj2 = datetime(2020, 4, 6)
duration = dt_obj - dt_obj2
print(f"The duration is {duration.days} days, {duration.seconds} seconds and {duration.microseconds} microseconds.")

dt_obj = datetime.now()
dt_obj = datetime.fromtimestamp(time())

print(dt_obj)

dt_obj = datetime.strptime("2018, 03, 05", "%Y, %m, %d")
dt_obj = datetime.strftime(dt_obj, "%m/%d")
print(dt_obj)
