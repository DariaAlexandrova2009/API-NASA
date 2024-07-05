TOKEN = '7457068545:AAFX0eTGzn0CfTybA2I3cU-D-J8sjwSAykE'
import telegram
from telegram.ext import Updater
import urllib3
from supporting_scripts import DIRECTORY
bot = telegram.Bot(token=TOKEN)
with open(f'{DIRECTORY}/image_1.jpg', 'rb') as file:
    bot.send_document(chat_id = '@spacephotoes', document=file)
    
