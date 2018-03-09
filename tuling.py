import requests
import json


TULING_TOKEN = "44b3067e9ba74faaaf809644e0d74dad"

def tulin(Content):
    url_api = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : TULING_TOKEN,
        'info'   : Content
        }
    s = requests.post(url_api, data=data).json()

    return s["text"]

