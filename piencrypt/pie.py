
from cryptography.fernet import Fernet
pie_hash = '03c1d04aeffd72151933b2295df5b484547e00ead9d001126aef03e6179a9332'

key = b'2PlCwYo0bGpbWBQ6onpmmKv9T8lshcJhI7R00NKxKpM='
clipher = Fernet(key)

class PiEncrypt:

    def __init__(self, loc):
        self.loc = loc
      
    # save the data of the picture as bytes 
    def get_data(self):
        with open(self.loc , 'rb') as f, open('backup.txt', 'wb') as b:
            r = f.read()
            b.write(r)

    # hides the disired data into the picture 
    def hide_data(self, data):
        self.data = data
        # encrypt the data
        encrypt_text = clipher.encrypt(bytes(pie_hash + self.data, encoding="ascii"))
        # save to the image
        with open(self.loc, 'ab') as f:
            f.write(bytes(pie_hash, encoding="ascii") + encrypt_text)

    # read the hidden data from the picture
    def read_data(self):
        with open(self.loc, 'rb') as f:
            content = f.read()
            list = content.split(bytes(pie_hash, encoding="ascii"))
            data = list[1]
            # dencrypt the text
            dencrypt_text = clipher.decrypt(data).decode("utf-8")
            # seperate by pie_hash
            output = dencrypt_text.split(pie_hash)
            return output[1]

    # revert the picture from the backup bytes file
    def revert(self):
        with open('backup.txt', 'rb') as f, open(self.loc, 'wb') as e:
            r = f.read()
            e.write(r)

if __name__ == '__main__':
    # print(key)
    # print(encrypt_text)
    # print(dencrypt_text)
    p = PiEncrypt('pic.png')
    p.get_data()
    p.hide_data("Hello this is piencrypt test")
    r = p.read_data()
    p.revert()
    print(r)
