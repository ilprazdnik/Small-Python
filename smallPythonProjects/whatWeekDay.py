#Whats the week day today?

import datetime

today = datetime.datetime.today()
weekDay = today.strftime('%A')

print(f'Today is {weekDay}')