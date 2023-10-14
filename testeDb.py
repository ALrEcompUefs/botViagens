from crawler import Crawler
from database import Database

if __name__ == "__main__":
    db = Database()
    #print(db.dB_find_by_id(2))
    #lista = db.dB_find_by_titulo('Rio ')
    #for data in lista:
    #    print(data,'\n\n')

    lista = db.dB_find_by_ano('2023')
    for data in lista:
        print(data,'\n\n')