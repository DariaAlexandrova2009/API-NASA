import telegram
from telegram.ext import Updater
import urllib3
import time
import random
import os
from supporting_scripts import DIRECTORY,send_file
from dotenv import load_dotenv
import argparse


def send_photos(delay):
    while True:
        for file in os.listdir(DIRECTORY):
            send_file(os.path.join(DIRECTORY,file),bot,tg_chat_id)
            time.sleep(delay)
        random.shuffle(os.listdir(DIRECTORY))
    

if __name__=='__main__':
    load_dotenv()
    token = os.environ['TG_BOT_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=token)
    parser = argparse.ArgumentParser(
        description='Программа отправляет фотографию из папки images'
    )
    parser.add_argument('-p', '--delay', help='Укажите время ожидания', default=3600, type=int)
    args = parser.parse_args()
    send_photos(args.delay)
