from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from typing import Dict
from typing import List

class Database:

    # construtor da classe
    def __init__(self):
        # inicializa sem o cliente
        self.client = None
        # carrega o dotenv
        load_dotenv()

    # conecta-se ao banco de dados
    def connect(self):
        try:
            # busca o env através do sistema operacional e cria o cliente para o database
            self.client = MongoClient(os.getenv("DB_URI"))
            self.client.admin.command('ping')
            db = self.client['banco_viagens']
        except Exception as e:
            print(e)
        finally:
            return db.viagens
    
    # fecha conexão com o banco de dados
    def close(self):
        if self.client:
            self.client.close()
    

    # Insere viagens na coleção de viagens
    # data é um dicionario com as viagens
    def dB_insert_viagens(self, data: list):
        # conecta-se ao banco de dados e obtém a colecção de viagens
        collection_viagens = self.connect()
        # percorre o dicionario viagem por viagem
        print(type(data))
        for viagem in data:
            #vefifica se a viagem ja existe no banco de dados
            # cada viagem possuí um titulo diferente
            print(viagem['titulo'],'\n\n')
            if not collection_viagens.find_one({'titulo': viagem['titulo']}):
                # insere nova instancia no banco de dados
                collection_viagens.insert_one({'id':viagem['id'],'titulo':viagem["titulo"],'pontifice': viagem['pontifice'],'ano':viagem['ano'],'destino':viagem['destino'],'url':viagem['url']})
                print('viagem inserida: ', viagem['titulo'],' com o id: ' , viagem['id'])
            else:
                # caso já exista no banco de dados então não ocorre a inserção
                print('viagem já existe no banco: ',viagem['titulo'],' com o id: ',viagem['id'])
        # após percorrer todos os novos dados fecha a conexão
        self.close()

    # faz a busca de uma viagem pelo id da viagem
    def dB_find_by_id(self, id:int):
        # conecta-se ao banco de dados e recebe a colecão 
        collection_viagens=self.connect()
        # como um id é unico a busca é feita usando findone
        viagem = collection_viagens.find_one({'id':id})
        # verifica se encontrou a instancia
        if not viagem:
            print('Nenhum objeto encontrado com o id:',id)
        else:
            print('Objeto encontrado:',viagem['titulo'],' com o id: ' , viagem['id'])
        return viagem
