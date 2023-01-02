# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone

data = datetime.now()
data1 = datetime.now(timezone('America/Sao_Paulo'))
data2 = datetime.now(timezone('Asia/Tokyo'))


data3 = datetime(2023, 1, 3, 7, 49, 50, tzinfo=timezone('Asia/Tokyo'))

print(data)
print(data1)
print(data2)
print(data3)
