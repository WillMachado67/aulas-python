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


# data = datetime(2023, 1, 1)
data2 = datetime(2023, 1, 3, 7, 49, 50)


data_str_data = '2023-01-03 07:49:50'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

data = datetime.strptime(data_str_data, data_str_fmt)

print(data)
print(data2)
