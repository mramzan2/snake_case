from datetime import datetime, date

def settlement_periods(date_str, granularity, location):

    dt = datetime.strptime(date_str, "%Y-%m-%d").date()


    hourly = 24
    half_hourly = 48


    if location.lower() == "uk":
        year = dt.year

        sundays_in_march = []
        for d in range(1, 32):
            try:
                check_date = datetime(year, 3, d).date()
                if check_date.weekday() == 6:
                    sundays_in_march.append(d)
            except:
                pass
        last_sunday_march = max(sundays_in_march)


        sundays_in_october = []
        for d in range(1, 32):
            try:
                check_date = datetime(year, 10, d).date()
                if check_date.weekday() == 6:
                    sundays_in_october.append(d)
            except:
                pass
        last_sunday_october = max(sundays_in_october)


        if dt == datetime(year, 3, last_sunday_march).date():

            hourly = 23
            half_hourly = 46
        elif dt == datetime(year, 10, last_sunday_october).date():

            hourly = 25
            half_hourly = 50


    if granularity.lower() in ["h", "hourly"]:
        return hourly
    elif granularity.lower() in ["hh", "half-hourly"]:
        return half_hourly
    else:
        raise ValueError("Granularity must be 'hourly' or 'half-hourly'")

