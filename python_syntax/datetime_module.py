import datetime

# d=datetime.date(2018,12,5)
# tday=datetime.date.today()

# print(tday.weekday())

td=datetime.timedelta(days=7)
# print(tday+t)

# bday=datetime.date(2019,12,1)
# (bday-tday).days
# print((bday-tday).total_seconds())

t=datetime.time(hour=12,minute=8,second=20)

dt=datetime.datetime(2019,12,5,8,12,4)
print(dt.date(),dt.time(),dt.hour,dt-td)