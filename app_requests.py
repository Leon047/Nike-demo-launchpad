import json
import requests
# from request_headers import *
from request_urls import *


class App_Requests:

    def base_request(self):
        for count, url in enumerate(url_shoes_for_choice):
            image = requests.get(url, stream=True, timeout=0.5)
            with BytesIO(image.content) as f:
                with Image.open(f) as out:
                    out.save('image/image{}.jpg'.format(count))


    def create_json(self):
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


if __name__=="__main__":
    App_Requests()

    #with open('payload.json') as f:
        #print(f.read())





