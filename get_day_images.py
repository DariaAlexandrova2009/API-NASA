from pathlib import Path
import requests
import os
from dotenv import load_dotenv
from supporting_scripts import DIRECTORY,get_file_extension,download_file


def get_apod(nasa_token):
    params = {
        'api_key': nasa_token, 
        'count': 30
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    response.raise_for_status()
    launches = response.json()
    for photo_number, photo in enumerate(launches):
        if photo['media_type'] == 'image':
            extension = get_file_extension(photo['url'])
            path = os.path.join(
                DIRECTORY,
                f"image_nasa_{photo_number}{extension}"
                )
            download_file(photo["url"], params, path)


if __name__=='__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    Path(DIRECTORY).mkdir(parents=True,exist_ok=True)
    get_apod(nasa_token)
    