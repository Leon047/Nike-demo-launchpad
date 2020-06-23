"""The module includes all http requests and work with json file conversions."""

import json
import io
import requests
from PIL import Image
from io import BytesIO
import request_data


def base_request():
    """Initial http request for source images from 'base_shoes_ur' list"""
    for count, url in enumerate(request_data.base_shoes_url):
        image = requests.get(url, stream=True, timeout=0.7)
        with BytesIO(image.content) as f:
            with Image.open(f) as out:
                out.save('image/image{}.jpg'.format(count))

def create_json():
    """ From the dictionary creates a JSON file """
    with open('payload.json', 'w') as f:
        json.dump(request_data.names_in_json, f, indent=2)

def post_request():
    """Sends user selected data in json format and gets json with url list."""
    with open('payload.json') as f:
        file_content = f.read()
        json_templates = json.loads(file_content)
    response =  requests.post(url = post_request_url,
                              json=json_templates,
                              stream=True)
    with open('sarsh_response.json', 'w') as data:
        json.dump(response.json(), data, indent=2)

def sarch_request():
    """
    From json takes a list of url and sends a request to download data from them
    """
    with open('sarsh_response.json', 'r') as f:
        data = json.loads(f.read())
    sarch_url_list = data['index']
    for count, url in enumerate(sarch_url_list):
        image = requests.get(url, stream=True, timeout=0.6)
        with BytesIO(image.content) as f:

            with Image.open(f) as out:
                out.save('image/image{}.jpg'.format(count+5))

if __name__=="__main__":
    post_request()
