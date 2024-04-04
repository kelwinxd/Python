from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta

dateInitial = datetime.strptime('20/12/2020', '%d/%m/%Y')
dateForm = dateInitial.strftime('%d/%m/%Y')
for i in dateForm:
    
    integer = int(dateForm)
    integer += relativedelta(days=30)
    print(integer)

print(integer)
