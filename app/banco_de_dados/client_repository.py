from app.banco_de_dados import client_repository
from app.modelos.client import Client

class Clienterepositorio:
    def __init__(self, banco_de_dados: BancoDeDadosLocal):
       self.banco_de_dados = banco_de_dados

       async def listar_clientes(self) -> list[Client]:
        with self.banco_de_dados.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id_, nome, email, telefone FROM clientes")
            rows = cursor.fetchall()
            clientes = [
               Client(id_=row[0], nome=row[1], email=row[2], telefone=row[3]) for row in rows
         ]

            return clientes