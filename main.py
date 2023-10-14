from crawler import Crawler
from database import Database
if __name__ == "__main__":
    crawler = Crawler()
    db = Database()

    links = crawler.extrair_links_viagens('https://www.vatican.va/content/francesco/pt.html')
    viagens = crawler.extrair_dados_viagens(links)
    viagens = crawler.formatar_dados(viagens)

    # mostra as viagens extraidas
    #for viagem in viagens['viagens']:
    #    print(viagem,'\n')

    # mostra o total de viagens extraidos
    print('Total de viagens:',len(viagens['viagens']))

    #print('\n\nInserindo no banco de dados')

    # insere as viagens no banco de dados
    #db.dB_insert_viagens(viagens['viagens'])
    # faz a busca por um id como exemplo
    print( db.dB_find_by_id(1))
    print( db.dB_find_by_id(2))
    print( db.dB_find_by_id(58))

    # faz busca por titulo
    