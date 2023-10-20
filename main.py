from crawler import Crawler
from database import Database
from bot import Bot
import schedule
import time

if __name__ == "__main__":
    crawler = Crawler()
    db = Database()
    bot = Bot()
    
    def job():

        print('|----- BUSCA POR NOVAS VIAGENS ----- |')
        # faz a extração de links para viagens
        links = crawler.extrair_links_viagens('https://www.vatican.va/content/francesco/pt.html')
        # extrai os dados das viagens
        viagens = crawler.extrair_dados_viagens(links)
        # formata os dados das viagens
        viagens = crawler.formatar_dados(viagens)

        # insere as viagens no banco de dados
        novas_viagens = db.dB_insert_viagens(viagens['viagens'])
        
        # faz as postagens 
        if len(novas_viagens) !=0:
            for viagem in novas_viagens:
                print('inserido')
                bot.post(viagem)
                time.sleep(1)
        
    schedule.every(1).minutes.do(job)

    while True:
        schedule.run_pending()
