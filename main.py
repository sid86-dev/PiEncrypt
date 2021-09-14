
class PEncryt:

    def __init__(self, loc):
        self.loc = loc
      
    # save the data of the picture as bytes 
    def get_data(self):
        with open(self.loc , 'rb') as f, open('binary.txt', 'wb') as b:
            r = f.read()
            b.write(r)

    # hides the disired data into the picture 
    def hide_data(self, data):
        self.data = data
        with open(self.loc, 'ab') as f:
            f.write(bytes("HERE" + self.data , encoding="ascii"))

    # read the hidden data from the picture
    def read_data(self):
        with open(self.loc, 'rb') as f:
            content = f.read()
            list = content.split(b'HERE')
            # print(f.read())
            return list[1].decode("utf-8")

    # revert the picture from the backup bytes file
    def revert(self):
        with open('binary.txt', 'rb') as f, open(self.loc, 'wb') as e:
            r = f.read()
            e.write(r)

if __name__ == '__main__':

    p = PEncryt('pic.jpg')
    p.get_data()
    p.revert()
    p.hide_data("Hello my name is SID")
    r = p.read_data()
    print(r)
