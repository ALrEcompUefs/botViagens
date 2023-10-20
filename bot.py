import tweepy
from dotenv import load_dotenv
import os

class Bot:
    
    # construtor
    def __init__(self):
        # carrega dotenv com as informações necessarias par autenticação
        load_dotenv()
        consumer_key= os.getenv('CONSUMER_KEY')
        consumer_secret= os.getenv('CONSUMER_SECRET')
        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret= os.getenv('ACCESS_TOKEN_SECRET')
        bearer_token = os.getenv('BEARER_TOEKN')

        #cria client responsavél pelas postagens
        self.client = tweepy.Client(
            consumer_key= consumer_key,
            consumer_secret = consumer_secret,
            access_token = access_token,
            access_token_secret=access_token_secret,
            bearer_token = bearer_token
        )

        #cria o autenticador da sessão do cliente
        auth = tweepy.OAuth1UserHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)

        # cria API
        self.api = tweepy.API(auth)

    # Função que faz uma postagem
    def post(self, data:dict):
        try:
            #cria tweet
            post ="{}\n\n Link:{}".format(data['titulo'],data['url'])
            self.client.create_tweet(text=post)
            return True
        except Exception as e:
            print(str(e))
            return False