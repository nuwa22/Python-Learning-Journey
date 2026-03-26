import datetime

now = datetime.datetime.now()

after_100_days = now + datetime.timedelta(days=100)
print("After 100 days:", after_100_days.strftime("%Y-%m-%d"))