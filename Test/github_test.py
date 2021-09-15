from piencrypt import pie

import requests
  
# api-endpoint
URL = "http://127.0.0.1:4000/test/sid86"
  
  
# sending get request and saving the response as response object
r = requests.get(url = URL)

data = r.json()

secret_code = data['PiEncrypt']

if secret_code == '8567a8a617f75a8ea43ce46aa8870dcf184728a58b5d60c7c3c2c83a5543dd76':
    test = 'pass'

else:
    'test' = 'failed'
    with open('pic.jpg', 'rb') as f:
        f.read()