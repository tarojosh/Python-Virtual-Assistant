# Check Time
from datetime import datetime


def invoke(query: str):
    # Return the hour:minute:seconds
    now = datetime.now()
    month = now.strftime("%B")
    # The time is {day of week}, {month} {day_number}, {hour}:{minute} {AM/PM}
    print(f"The time is {now}")