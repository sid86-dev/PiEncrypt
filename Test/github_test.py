from piencrypt import pie

import requests
  
# api-endpoint
URL = "https://piencrypt.herokuapp.com/test/sid86"
  
  
# sending get request and saving the response as response object
r = requests.get(url = URL)


data = r.json()

secret_code = data['PiEncrypt']


if secret_code == '03c1d04aeffd72151933b2295df5b484547e00ead9d001126aef03e6179a9332':
    num = 1 + 2


else:
    test = 'failed'
    with open('pic.jpg', 'rb') as f:
        f.read()