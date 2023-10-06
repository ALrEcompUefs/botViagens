import urllib.request
from bs4 import BeautifulSoup
import json

# A classe crawler implementa o web crawler que faz a busca e extração dos dados das viagens
class Crawler:

    # construtor
    def __init__(self):
        pass          
    # O método crawler_request_page faz a requisição get para obter a pagina html
    def crawler_request_page(self, url):
        # utiliza a biblioteca requests para 
        page = urllib.request.urlopen(str(url))
        # transforma em string e corrige a codifiação
        html = str(page.read().decode('utf-8'))
        # criar o parser html
        soup = BeautifulSoup(html, 'lxml') 
        # retorna o parser
        return soup
    
    # o método extrair_links_viagens faz a busca pelos links que fazem referencia as viagens apostolicas
    def extrair_links_viagens(self, url_page):
        # conjunto para os links buscados
        # é utilizando um set para evitar urls duplicadas
        lista_de_links = set()
        # obtém o parser para a pagina solicitada
        page_viagens = self.crawler_request_page(url_page)
        # obtém os titulos e links das viagens
        for ref in page_viagens.find_all('ul'):
            #
            if( ref.get("path") =="travels" != -1): 
                for ul in ref.find_all('ul'):
                    # Busca os links e insere na lista 
                    for a in ul.find_all('a'):
                        # concatena o primeiro termo para gerar as urls
                        aux = "https://www.vatican.va"+str(a.get("href"))
                        lista_de_links.add(aux)
        # retorna lista com urls das viagens
        return lista_de_links
    
    # o método extrair_dados_viagens extrai os dados das viagens e insere em dicionario
    def extrair_dados_viagens(self,lista_de_links: set):
        # cria lista para salvar viagens
        colecao = list()
        # cria dicionario para viagens e inicializa
        viagens = dict()
        viagens["tipo"]="viagens"
        # viagens possui um array para dicionarios do tipo 
        # dados[id,titulo,link]
        viagens["viagens"]=[]
        # id unico para indentificar os elementos a partir de 1
        # precisa se alterado para uma opçãao mais eficiente e controlada
        id = 1
        # Contador de operações
        count = 0

        for link in lista_de_links:
            # obtém o parser para viagens registradas por ano
            parser_pagina = self.crawler_request_page(link)
            #print(link,'\n')
            # dentro do html a div 'documento' que possui os titulos das viagens
            campo = parser_pagina.find('div',{'class':'documento'})
            for h1 in campo.find_all('h1'):
                # Obtém titulo da viagem
                titulo = h1.text
                # Inicia url como vazia
                url = 'none'
                # busca a tag de endereçamento, só vai existir uma
                ref = h1.find('a')
                # se encontrou uma tag a então pode retirar a ur
                if ref.__class__ != type(None):
                    url = "https://www.vatican.va" + str( ref.get('href'))
                # insere na colecao o novo item
                colecao.append({'id':id,"titulo":titulo,'link':url})
                id = id+1
                count = count+1
        print('Total de viagens',count)
        # insere as viagens no campo da viagens do dicionario viagens
        viagens["viagens"]= colecao
        return viagens

    # o método formatar_dados faz a extração e formatação dos dados ja extraidos
    def formatar_dados(self, viagens:dict):
        lista_viagens = viagens['viagens']
        colecao = []
        # itera por cada item da lista e faz a extração
        for viagem in lista_viagens:
            # divide a string em tokens usando o pivo do '/'
            tokens = str(viagem['link']).split('/')
            # extrai o pontifice da url
            if len(tokens) != 1:
                ponticie = tokens[4]
                ponticie = "Francesco" if ponticie == "francesco" else "none"

                #obtém ano da viagem
                ano = str(tokens[7]).split('.')[0]

                if "/inside.index" in viagem['link'] or "/outside.index" in viagem['link']:
                    #print("não é viagem")
                    pass
                else:
                    if 'francesco' in tokens:
                        if(len(tokens)>=11):
                            destino = str(tokens[10]).split('.html')[0]
                        
                            if "papa-francesco" in destino:
                                destino = destino.split("papa-francesco-")
                                destino=destino[1]
                        #print(destino)
                    colecao.append({'id':viagem['id'],'titulo':viagem["titulo"],'pontifice':ponticie,'ano':ano,'destino':destino,'url':viagem['link']})
        viagens['viagens']=colecao
        return viagens
    

    