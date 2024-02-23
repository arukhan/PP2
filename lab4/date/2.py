from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday.strftime("%x"))
print(today.strftime("%x"))
print(tomorrow.strftime("%x"))