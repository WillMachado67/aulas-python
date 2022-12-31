# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None: # type anotation
        self.mensagem = mensagem


    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self):
        print('Email: enviando: ', self.mensagem)


class NotificacaoSMS(Notificacao):
    def enviar(self):
        print('SMS: enviando: ', self.mensagem)


# n = NotificacaoEmail('Funcionou')
# n.enviar()

n = Notificacao('ola')