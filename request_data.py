"""The module contains all URLs for requests."""

post_request_url = "https://c25nnqnhgk.execute-api.us-east-1.amazonaws.com/v0/predict"

# base image urls
base_shoes_url = [
    "https://content.adidas.co.in/static/Product-CM7531/Unisex_OUTDOOR_SANDALS_CM7531_1.jpg",
    "https://cdn.shopify.com/s/files/1/0080/1374/2161/products/product-image-897958210_640x.jpg?v=1571713841",
    "https://cdn.chamaripashoes.com/media/catalog/product/cache/9/image/9df78eab33525d08d6e5fb8d27136e95/1/_/1_8_3.jpg",
    "https://ae01.alicdn.com/kf/HTB1EyKjaI_vK1Rjy0Foq6xIxVXah.jpg_q50.jpg",
    "https://www.converse.com/dw/image/v2/BCZC_PRD/on/demandware.static/-/Sites-cnv-master-catalog/default/dwb9eb8c43/images/a_107/167708C_A_107X1.jpg",
    "https://images.vans.com/is/image/Vans/EYEW00-HERO?$583x583$"
]

# User entered data
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

# Converting data to json form
names_in_json = { "all_data": all_data,
                  "add_words": add_positive_attributes,
                  "sub_words": add_negative_attributes,
                  "casual": casual,
                  "sport": sport,
                  "gender": gender,
                  "model_id": model_id,
                  "topk": topk,
                  "url": image_url,
                   0: sub_url
                 }

# label and image names 
label_data = {  "photo_0": "image/image0.jpg",
                "photo_1": "image/image1.jpg",
                "photo_2": "image/image2.jpg",
                "photo_3": "image/image3.jpg",
                "photo_4": "image/image4.jpg",
                "photo_5": "image/image5.jpg",
                "photo_6": "image/image6.jpg",
                "photo_7": "image/image7.jpg",
                "photo_8": "image/image8.jpg",
                "photo_9": "image/image9.jpg",
                "photo_10": "image/image10.jpg"
              }
