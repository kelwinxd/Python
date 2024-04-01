from datetime import datetime
from pytz import timezone


if __name__ == '__main__':
 data = datetime.now(timezone('Asia/Tokyo'))
 formated = data.strftime('%H:%M')
 print(formated)