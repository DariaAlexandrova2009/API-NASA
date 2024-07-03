import requests
import os
import urllib.request
import urllib.parse

DIRECTORY = 'images'


def download_file(url, params, path):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_file_extension(file_url):
    encoded_string = urllib.parse.unquote(file_url)
    url_parts = urllib.parse.urlsplit(encoded_string)
    path = url_parts.path
    file_path, file_extension = os.path.splitext(path)
    return file_extension


