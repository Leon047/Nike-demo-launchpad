import json
import requests
# from request_headers import *
from request_urls import *


class App_Requests:

    def request_shoes_for_choice(self):
        for count, url in enumerate(url_shoes_for_choice):
            image = requests.get(url, stream=True, timeout=0.5)
            with BytesIO(image.content) as f:
                with Image.open(f) as out:
                    out.save('image/image{}.jpg'.format(count))

if __name__=="__main__":
    App_Requests()
