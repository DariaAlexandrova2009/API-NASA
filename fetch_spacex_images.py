import argparse
from pathlib import Path
import requests
import os.path
import logging
from supporting_scripts import DIRECTORY, download_file


def fetch_spacex_last_launch(lounch_id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{lounch_id}')
    response.raise_for_status()
    photos_urls = response.json()['links']['flickr']['original']
    if not photos_urls:
        logging.warning('Ничего не скачалось! Файлы не были получены...')
    for photo_number, photo_url in enumerate(photos_urls):
        path = os.path.join(DIRECTORY, f"image_{photo_number}.jpg")
        download_file(photo_url, {}, path)


if __name__=='__main__':
    Path(DIRECTORY).mkdir(parents=True,exist_ok=True)
    parser = argparse.ArgumentParser(description='Программа скачивает фотографии с запуска ракет.')
    parser.add_argument('-i', '--id', help='ID запуска', default='latest')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)