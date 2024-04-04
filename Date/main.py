from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta


if __name__ == '__main__':
 #timezone
 data = datetime.now(timezone('Asia/Tokyo'))
 formated = data.strftime('%H:%M')
 print(formated)

 today = datetime.now()

 #relative delta
 #delta = today + relativedelta(days=24)
 formatedDay = today.strftime('%d/%m/%Y')
 
 print(formatedDay)

 birth = datetime.strptime('28/04/2024', '%d/%m/%Y')
 until = birth - today
 print(f'Its {until} days until your birthday ')