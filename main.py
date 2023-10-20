from crawler import Crawler
from database import Database
from bot import Bot

if __name__ == "__main__":
    crawler = Crawler()
    db = Database()
    bot = Bot()
    
    links = crawler.extrair_links_viagens('https://www.vatican.va/content/francesco/pt.html')
    viagens = crawler.extrair_dados_viagens(links)
    viagens = crawler.formatar_dados(viagens)

    # mostra as viagens extraidas
    for viagem in viagens['viagens']:
        print(viagem,'\n')

    # mostra o total de viagens extraidos
    print('Total de viagens:',len(viagens['viagens']))

    print('\n\nInserindo no banco de dados')

    # insere as viagens no banco de dados
    novas_viagens = db.dB_insert_viagens(viagens['viagens'])
    
    if len(novas_viagens) !=0:
        for viagem in novas_viagens:
            print('inserido')
            bot.post(viagem)

    '''    
    # faz a busca por um id como exemplo
    print('\nBusca por id')
    print( db.dB_find_by_id(1))
    print( db.dB_find_by_id(2))
    print( db.dB_find_by_id(58))

    # faz busca por titulo
    print('\nBusca por titulo')
    lista = db.dB_find_by_titulo('Rio ')
    for vg in lista:
        print(vg)
    
    # faz a busca por ano
    print('\nBusca por ano')
    lista = db.dB_find_by_ano('2023')
    for vg in lista:
        print(vg)
    '''