from crawler import Crawler

if __name__ == "__main__":
    crawler = Crawler()
    links = crawler.extrair_links_viagens('https://www.vatican.va/content/francesco/pt.html')
    viagens = crawler.extrair_dados_viagens(links)
    viagens = crawler.formatar_dados(viagens)

    
    for viagem in viagens['viagens']:
        print(viagem,'\n')
    print('Total de viagens:',len(viagens['viagens']))