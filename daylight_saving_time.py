from datetime import datetime

year = 2025
march_days = range(1, 32)

sundays_in_march = []

for d in march_days:
    date = datetime(year, 3, d)
    if date.weekday() == 6:
        sundays_in_march.append(d)

last_sunday_march = max(sundays_in_march)
oct_days = range(1, 32)
sundays_in_oct = []

for d in oct_days:
    date = datetime(year, 10, d)
    if date.weekday() == 6:
        sundays_in_oct.append(d)
last_sunday_oct = max(sundays_in_oct)


