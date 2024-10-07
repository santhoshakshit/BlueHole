import datetime
def get_current_time_and_date():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
    time = now.strftime("%H:%M:%S")  # Format: HH:MM:SS
    return f"Today's date is {date} and the current time is {time}."
