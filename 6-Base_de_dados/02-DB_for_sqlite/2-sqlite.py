import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DIR_BD = ROOT_DIR / 'agenda.db'


class AgendaDB:
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def inserir(self, nome, telefone):
        consulta = "INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)"
        self.cursor.execute(consulta, (nome, telefone))
        self.conexao.commit()

    def editar(self, nome, telefone, id):
        consulta = "UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?"
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conexao.commit()

    def excluir(self, id):
        consulta = "DELETE FROM agenda WHERE id=?"
        self.cursor.execute(consulta, (id,))
        self.conexao.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.conexao.close()
        self.cursor.close()


if __name__ == '__main__':
    agenda = AgendaDB(DIR_BD)
    # agenda.inserir('Luiz', '111111')
    # agenda.inserir('João', '2222222')
    # agenda.inserir('Pedro', '333333')
    # agenda.inserir('Maria', '444444')
    # agenda.inserir('José', '555555')
    # agenda.inserir('Tiago', '666666')
    # agenda.inserir('Luiz', '777777')

    agenda.editar('Fabio', '212121', 7)
    agenda.excluir(10)

    # agenda.inserir('José Maria', '555556')
    # agenda.inserir('José Antonio', '555557')
    # agenda.inserir('José Felipe', '555558')
    # agenda.inserir('Maria José', '555559')
    # agenda.inserir('R. José', '555550')
    # agenda.inserir('T. José Carlos', '555551')

    # agenda.buscar('Tiago')
    
    agenda.listar()
