from time import sleep
from threading import Thread
import os


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t = Thread(target=vai_demorar, args=('Acabou!', 5))
t.start()
t.join()

frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
while t.is_alive():
    for f in frames:
        print('\rCarregando ' + f, end='')
        sleep(0.1)
        if not t.is_alive():
            break
