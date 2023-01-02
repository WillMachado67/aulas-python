# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

delta = timedelta(days=8)

print(data_fim - delta)
