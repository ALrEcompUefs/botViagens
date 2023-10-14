from crawler import Crawler
from database import Database

if __name__ == "__main__":
    db = Database()
    print(db.dB_find_by_id(2))