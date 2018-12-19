import datetime

# naive datetime is easier to work and aware dates and time will have timezone etc.

d = datetime.date(2016, 7, 24)
print(d)

# pass in integers without leading 0s like 07 will fail

# todays local date
tday = datetime.date.today()
print(tday)

print(tday.year)
print(tday.day)
print(tday.weekday())   # Monday is 0
print(tday.isoweekday())  # Monday is 1

#time delta from one week away

tdelta = datetime.timedelta(days=7)
#what the date would be 7 days from now

print(tday + tdelta)

# add or subtract timedelta from a date
# how many days are there to my birthday

bday = datetime.date(2016, 9, 24)

till_bday = bday - tday
print(till_bday)
print(till_bday.total_seconds())

# let us look at time, hours, min, sec, ms
t = datetime.time(9, 30, 45, 100000)
print(t.hour)

t = datetime.datetime(2016, 7, 26, 12, 30, 45, 10000)  # give access to dates and hours
print(dt.date())
print(dt.time())
print(dt.year)

tdelta = datetime.timedelta(days=7)
print(dt + tdelta)

tdelta = datetime.timedelta(hours=7)
print(dt + tdelta)

# to get timezone use packate pytz
import datetime
import pytz

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

# to print US mountain time

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)



# to print all timezones

for tz in pytz.all_timezones:
    print(tz)

# to create a naive time to timezone time

