from time import sleep
from threading import Thread


class MeuThred(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThred('thred 1', 5)
t2 = MeuThred('Ola!!!', 8)
t3 = MeuThred('Esta acabando', 17)
t2.start()
t1.start()
t3.start()


for i in range(1, 20):
    print(i)
    sleep(1)
