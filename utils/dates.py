from datetime import datetime, timezone, timedelta

def calculate_today():
    date_today = datetime.now()
    time_zone = timezone(timedelta(hours=-10))
    return date_today.astimezone(time_zone)