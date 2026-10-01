#ex1
from datetime import datetime
now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(f"today is: {day}/{month}/{year}, time is: {hour}:{minute}, timestamp: {timestamp}")

#ex2
from time import strftime, strptime
formatted = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted)
print(type(formatted)) #<class 'str'>

#ex3
today_str = "05 December 2019"
today_obj = strptime(today_str, "%d %B %Y")
print(today_obj) #returns <class 'time.struct_time'>
#time.struct_time(tm_year=2019, tm_mon=12, tm_mday=5, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=339, tm_isdst=-1)

#ex4
new_year = datetime(year=2027, month=1, day=1, hour=0, minute=0, second=0)
diff = new_year - now
print(f"time left till new year: {diff}")

#ex5
t1 = datetime(year=1970, month=1, day=1)
diff2 = now - t1
print(f"Difference between now and 1970: {diff2}")

#ex6
'''
Datetime module can also be used for:
1. handling different meeting timezone, i.e: meeting today 18:00PM UTC+8 is X time in UTC+2
2. Logging of software: compilation or firmware installation - Similar to timestamp of activities
3. Some sort of version control? Comparing multiple file names based on timestamp and size of data and changes?
4. AI model training time
'''