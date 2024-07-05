import telegram
from telegram.ext import Updater
import random
import os
from supporting_scripts import DIRECTORY,send_file
from dotenv import load_dotenv
import argparse



if __name__=='__main__':
    load_dotenv()
    token = os.environ['TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=token)
    files = os.listdir(DIRECTORY)
    parser = argparse.ArgumentParser(
        description='Программа отправляет фотографию из папки images'
    )
    parser.add_argument('-p', '--photo', help='Укажите фото которое нужно отправить', default=random.choice(files))
    args = parser.parse_args()
    send_file(os.path.join(DIRECTORY, args.photo),bot,tg_chat_id)