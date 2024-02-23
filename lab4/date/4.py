from datetime import datetime

def difference(date1, date2):
    time_difference = date2 - date1
    seconds_difference = time_difference.total_seconds()
    return seconds_difference


date1 = datetime(2024, 2, 21, 11, 8, 23)
date2 = datetime(2024, 2, 21, 17, 21, 2)

difference_seconds = difference(date1, date2)

print("Difference in seconds:", difference_seconds)
