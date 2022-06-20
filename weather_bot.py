from distutils import command
from aiohttp import request
from sympy import arg, content
## Weather Bot
import telepot
import requests
from bs4 import BeautifulSoup
import urllib.request

TOKEN = '5213699570:AAEaAPz5oWzsAqT_XoLxX2ZRRPyeAmyv_-U'

def get_weather(where):
  weather = ""
  url = f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={where}+날씨"
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  
  temperature = soup.find('div',"temperature_text").get_text()
  indicator = soup.find('p',"summary").get_text()
  rain_prob = soup.find('dd', 'desc').get_text()

  weather = f"(Weather) {temperature}\r\n{indicator}\r\n강수확률: {rain_prob}"

  return weather

def handler(msg):
  content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
  print(msg)
  print('-' * 36)

  if content_type == 'text':
    str_message = msg["text"]
    if str_message[0:1] == '/':
      args = str_message.split(" ")
      command = args[0]
      del args[0]

      if command == '/날씨':
        w = " ".join(args)
        weather = get_weather(w)
        bot.sendMessage(chat_id, weather)
        
bot = telepot.Bot(TOKEN)
bot.message_loop(handler, run_forever=True)
    
