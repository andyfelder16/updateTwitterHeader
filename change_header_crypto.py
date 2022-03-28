from os import write
import tweepy
import time
from PIL import Image, ImageFont, ImageDraw 
import requests
from datetime import datetime

CONSUMER_KEY = '##############' #API KEY
CONSUMER_SECRET = '##############' #API SECRET KEY
ACCESS_KEY = '##############-##############' #access token 
ACCESS_SECRET = '##############' #access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
url = "https://api.binance.com/api/v3/ticker/price?symbol="

def get_latest_crypto_price(crypto):
    # requesting data from url
    data = requests.get(url+crypto)  
    data = data.json()
    symbol = data['symbol']
    price = round(float(data['price']),2)
    print(symbol + ": " + str(price))
    return(symbol, str(price))

def update_twitter_header():
    api.update_profile_banner('resultCrypto.png')

def update_price_image():
    my_image = Image.open("baseCryptoPrice.png")
    title_font = ImageFont.truetype('arial.ttf', 28)
    title_font2 = ImageFont.truetype('arial.ttf', 18)
    image_editable = ImageDraw.Draw(my_image)

    btc_price = get_latest_crypto_price("BTCUSDT")[1]
    eth_price = get_latest_crypto_price("ETHUSDT")[1]
    bnb_price = get_latest_crypto_price("BNBUSDT")[1]
    sol_price = get_latest_crypto_price("SOLUSDT")[1]

    # image_editable.text((x, y),"Sample Text",(r,g,b))
    image_editable.text((200,215), btc_price, (237, 230, 211), font=title_font)
    image_editable.text((480,215), eth_price, (237, 230, 211), font=title_font)
    image_editable.text((760,215), bnb_price, (237, 230, 211), font=title_font)
    image_editable.text((1030,215), sol_price, (237, 230, 211), font=title_font)

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")

    image_editable.text((1146,363), date_time, (237, 230, 211), font=title_font2)
    my_image.save("resultCrypto.png")

#get_latest_crypto_price('BTCUSDT')

def main():
    while True:
        update_price_image()
        update_twitter_header()
        time.sleep(30)

main()
#update_price_image()

