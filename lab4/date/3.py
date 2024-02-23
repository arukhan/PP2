from datetime import datetime

date = datetime.now()

drop_microseconds = date.replace(microsecond=0)

print(drop_microseconds)
