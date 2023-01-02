from eletronicos import Smartphone
from log import LOG_FILE
import os

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')


galaxy_s.ligar()
iphone.desligado()



# os.remove(LOG_FILE)
