from icecream import ic

def manipulate_datetime():
    """
    # Manipulate datetime
    """
    import datetime
    
    ic(datetime.date(2026, 1, 1))

    mydate = datetime.date(2026, 2, 1)
    ic(mydate)
    ic(mydate.year)
    ic(mydate.month)
    ic(mydate.day)
    ic(mydate.weekday())

    # datetime in string format
    ic(mydate.isoformat())
    ic(str(mydate))
    ic(mydate.strftime('%Y/%m/%d'))
    ic(mydate.strftime('%Y/%b/%d (%a)'))

    ic(datetime.date.today())

    # Manipulate time object
    ic(datetime.time())
    ic(datetime.time(12, 35, 50))
    ic(datetime.time(minute=10))
    ic(datetime.time(second=10))
    ic(datetime.time(microsecond=10))

    mytime = datetime.time(12, 35, 50)
    ic(mytime)
    ic(mytime.hour, mytime.minute, mytime.second, mytime.microsecond)

    # time in string format
    ic(mytime.isoformat())
    ic(mytime.strftime('%H:%M'))
    ic(str(mytime))

    # Manipulate datetime object
    ic(datetime.datetime.today())

    today = datetime.datetime.today()
    ic(today)
    ic(today.date())
    ic(today.time())

    # datetime in string format
    ic(today.isoformat())
    ic(today.strftime('%Y/%m/%d'))

    # Manipulate timedelta object
    today = datetime.date.today()
    ic(today)

    newdate = datetime.date(2027, 3, 16)
    ic(newdate)

    ic(newdate - today)

    # build a week timedelta
    week = datetime.timedelta(days=7)
    ic(week)
    ic(today + week)
    ic(today + week * 2)
    ic(today - week)

def manipulate_time():
    """
    Manipulate time
    """
    import time
    ic(time.gmtime())
    ic(time.localtime())
    ic(time.strftime('%Y-%m-%d', time.localtime()))
    ic(time.time())

    # Manipulate struct_time structure
    # get local time
    local = time.localtime()
    # get utc time
    utc = time.gmtime()
    ic(local)
    ic(utc)

    ic(local.tm_mday)
    ic(local.tm_hour)
    ic(utc.tm_mday)
    ic(utc.tm_hour)

def manipulate_dateutil_parse():
    """
    Manipulate dateutil parse
    """
    import datetime
    from dateutil.parser import parse
    ic(parse('2026/02/01 20:10:50'))
    ic(parse('2026-02-01'))
    ic(parse('20260201'))
    ic(parse('20260201201050'))
    ic(parse('Tue, 17 Mar 2026 10:20:30 JST'))
    ic(parse('Tue, 17 Mar 2026 10:20:30 GMT'))

    # Use default to be the base of datetime parser
    default = datetime.datetime(2026, 3, 17)
    ic(default)
    ic(parse('Tue, 17 Mar 2026 10:20:30', default=default))
    ic(parse('Tue, 10:20:30', default=default))
    ic(parse('10:20:30', default=default))
    ic(parse('10:20', default=default))

    # Use parse() to verify date and time
    ic(parse('1/2/3'))
    ic(parse('1/2/3', dayfirst=True))
    ic(parse('1/2/3', yearfirst=True))
    ic(parse('15/2/33'))
    ic(parse('15/2/33', yearfirst=True))
    ic(parse('15/2/33', dayfirst=True))

def manipulate_dateutil_relativedelta():
    """
    Manipulate dateutil relativedelta
    """
    import datetime
    from dateutil.relativedelta import relativedelta
    from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU

    now = datetime.datetime.now()
    ic(now)

    today = datetime.date.today()
    ic(today)

    # after 1 month
    ic(now + relativedelta(months=+1))

    # 1 week after a month ago
    ic(now + relativedelta(months=-1, weeks=1))

    # 10 o'clock a month from now
    ic(today + relativedelta(months=+1, hour=10))

    # Set day of week
    # next Friday
    ic(today + relativedelta(weekday=FR))
    # the last Friday of this month
    ic(today + relativedelta(day=31, weekday=FR(-1)))
    # next Tuesday (including today if today is Tuesday)
    ic(today + relativedelta(weekday=TU(+1)))
    # next Tuesday (excluding today if today is Tuesday)
    ic(today + relativedelta(days=+1, weekday=TU(+1)))

    # Set day of year
    # the 100th day in year 2026
    ic(datetime.date(2026, 1, 1) + relativedelta(yearday=100))

    # nothing to do with starting date, always starts from the start of the year
    ic(datetime.date(2026, 12, 1) + relativedelta(yearday=100))

    # the 100th day in leap year 2012 including leap day
    ic(datetime.date(2012, 1, 1) + relativedelta(yearday=100))

    # the 100th day in leap year 2012 excluding leap day
    ic(datetime.date(2012, 1, 1) + relativedelta(nlyearday=100))

    # Get date delta
    ic(relativedelta(datetime.date(2026, 1, 1), today))
    ic(relativedelta(datetime.date(2027, 1, 1), today))

def manipulate_dateutil_rrule():
    import datetime
    from dateutil.rrule import rrule
    from dateutil.rrule import DAILY, WEEKLY, MONTHLY
    from dateutil.rrule import MO, TU, WE, TH, FR, SA, SU
    
    start = datetime.datetime(2026, 1, 1)
    ic(start)
    # consective 5 days
    ic(list(rrule(DAILY, count=5, dtstart=start)))

    # consective days until the given date
    ic(list(rrule(DAILY, dtstart=start, until=datetime.datetime(2026, 5, 31))))
    
    # every Tuesday and Thursday
    # wkst: start of week e.g. normally SU or MO, but others like TH are also allowed
    ic(list(rrule(WEEKLY, count=8, wkst=SU, byweekday=(TU, TH), dtstart=start)))
    
    # all weekdays until the given date
    ic(list(rrule(WEEKLY, until=datetime.date(2026, 3, 31), wkst=MO, byweekday=(MO, TU, WE, TH, FR), dtstart=start)))

    # last Friday of each month
    ic(list(rrule(MONTHLY, count=3, byweekday=FR(-1), dtstart=start)))

    # every two weeks
    ic(list(rrule(WEEKLY, interval=2, count=3, dtstart=start)))

def manipulate_pytz():
    """
    Manipulate timezone
    """
    from datetime import datetime
    import pytz

    fmt: str = "%Y-%m-%d %H:%M:%S %Z%z"
    taipei = pytz.timezone('Asia/Taipei')
    eastern = pytz.timezone('US/Eastern')
    
    taipei_dt = taipei.localize(datetime(2025, 1, 20, 12, 30))
    ic(taipei_dt.strftime(fmt))

    eastern_dt = taipei_dt.astimezone(eastern)
    ic(eastern_dt.strftime(fmt))

    # Convert to US Eastern Daylight Saving Time
    taipei_dt = taipei.localize(datetime(2025, 6, 20, 12, 30))
    ic(taipei_dt.strftime(fmt))
    eastern_dt = taipei_dt.astimezone(eastern)
    ic(eastern_dt.strftime(fmt))

    jan = datetime(2025, 1, 1)
    jun = datetime(2025, 6, 1)
    ic(eastern.utcoffset(jan))
    ic(eastern.utcoffset(jun))

    ic(eastern.dst(jan))
    ic(eastern.dst(jun))
    ic(eastern.tzname(jun))
    ic(eastern.tzname(jan))

    ic(pytz.country_timezones['nz'])
    ic(pytz.country_names['nz'])
    ic(len(pytz.all_timezones))
    ic(len(pytz.common_timezones))
    ic('Singapore' in pytz.all_timezones_set)
    ic('Singapore' in pytz.common_timezones_set)
    ic('Asia/Singapore' in pytz.common_timezones_set)

if __name__ == "__main__":
    # manipulate_datetime()
    # manipulate_time()
    # manipulate_dateutil_parse()
    # manipulate_dateutil_relativedelta()
    # manipulate_dateutil_rrule()
    manipulate_pytz()
