from datetime import datetime, timedelta
date = datetime.now()
updated= date - timedelta(days=5)
print(updated.strftime("%x"))