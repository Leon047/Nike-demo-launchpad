"""The module includes all http requests and work with json file conversions."""

import json
import io
import requests
from PIL import Image
from io import BytesIO
from request_urls import *


def base_request():
    """Initial http request for source images from 'base_shoes_ur' list"""
    for count, url in enumerate(base_shoes_url):
        image = requests.get(url, stream=True, timeout=0.6)
        with BytesIO(image.content) as f:
            with Image.open(f) as out:
                out.save('image/image{}.jpg'.format(count))

def create_json():
    """
    Fills and creates a JSON file with subsequentstoragein the root directory.
    """
    all_data = {}
    add_positive_attributes = []
    add_negative_attributes = []
    casual = "False"
    sport = "False"
    gender = "All"
    model_id = "v3"
    topk = 5
    image_url = ["https://ae01.alicdn.com/kf/HTB1EyKjaI_vK1Rjy0Foq6xIxVXah.jpg_q50.jpg"]
    sub_url = "https://ae01.alicdn.com/kf/HTB1EyKjaI_vK1Rjy0Foq6xIxVXah.jpg_q50.jpg"
    names_in_json = { "all_data": all_data,
                      "add_words": add_positive_attributes,
                      "sub_words": add_negative_attributes,
                      "casual": casual,
                      "sport": sport,
                      "gender": gender,
                      "model_id": model_id,
                      "topk": topk,
                      "url": image_url,
                       0: sub_url }
    with open('payload.json', 'w') as f:
        json.dump(names_in_json, f, indent=2)

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
