from asyncore import dispatcher
from email.message import Message
## Echo Bot
import telepot
from telepot.loop import MessageLoop

with open("./data/token.txt", "r") as f:
    TOKEN = f.read()

def handle(msg):
  content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
  print(msg)
  print('-' * 36)

  if content_type == 'text':
    bot.sendMessage(chat_id, '(Echo)' + msg['text'])

bot = telepot.Bot(TOKEN)
# bot.message_loop(handle, run_forever=True)
MessageLoop(bot, handle).run_forever()

print("Listening...")

import time
while True:
  time.sleep(10)


