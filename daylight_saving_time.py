import sys
import random
import math
import calendar
from datetime import datetime, timedelta

def get_last_sunday(year, month):
    month_calendar = calendar.monthcalendar(year, month)
    last_week = month_calendar[-1]
    if last_week[calendar.SUNDAY] == 0:
        last_sunday = month_calendar[-2][calendar.SUNDAY]
    else:
        last_sunday = last_week[calendar.SUNDAY]
    return last_sunday

def get_num_periods(date_str, location):
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    year = date.year
    num_periods = 48
    last_sunday_march = get_last_sunday(year, 3)
    last_sunday_october = get_last_sunday(year, 10)
    if location.lower() in ["uk", "france"]:
        dst_start = datetime(year, 3, last_sunday_march).date()
        dst_end = datetime(year, 10, last_sunday_october).date()
        if date == dst_start:
            num_periods = 46
        elif date == dst_end:
            num_periods = 50
    return num_periods

def seasonal_factor(date_str, amplitude=0.20):
    dt = datetime.strptime(date_str, "%Y-%m-%d").date()
    day_of_year = dt.timetuple().tm_yday
    theta = 2 * math.pi * (day_of_year - 1) / 365
    return 1.0 + amplitude * math.cos(theta)
def generate_prices(num_periods, date_str):
    base_price = 50.0
    season_mult = seasonal_factor(date_str)
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    weekday = date.weekday()
    prices = []
    for i in range(num_periods):
        peak_factor = math.sin((i / num_periods) * 2 * math.pi * 2) + 1
        daily_profile = 0.5 + 0.5 * peak_factor
        weekend_factor = 0.85 if weekday >= 5 else 1.0
        noise = random.uniform(0.95, 1.05)
        price = base_price * season_mult * daily_profile * weekend_factor + noise
        prices.append(round(price, 2))
    return prices

def main():
    if len(sys.argv) < 3:
        print("Usage: python price_generator.py <YYYY-MM-DD> <UK|France>")
        sys.exit(1)

    date_str = sys.argv[1]
    location = sys.argv[2]
    num_periods = get_num_periods(date_str, location)
    prices = generate_prices(num_periods, date_str)
    print(f"\n Date: {date_str}")
    print(f"Location: {location}")
    print(f"Settlement Periods (half-hourly): {num_periods}")
    print(f"Seasonal Factor: {round(seasonal_factor(date_str), 3)}")
    print("\n Sample Prices:")
    print(prices[:12], "...")
if __name__ == "__main__":
    main()