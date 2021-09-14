# save the data of the picture as bytes 
def get_data(loc):
    with open(loc , 'rb') as f, open('binary.txt', 'wb') as b:
        r = f.read()
        b.write(r)
# hides the disired data into the picture 
def hide_data(loc, data):
    with open(loc, 'ab') as f:
        f.write(bytes("HERE" + data , encoding="ascii"))
# read the hidden data from the picture
def read_data(loc):
    with open(loc, 'rb') as f:
        content = f.read()
        list = content.split(b'HERE')
        # print(f.read())
        return list[1].decode("utf-8")
# revert the picture from the backup bytes file
def revert(loc):
    with open('binary.txt', 'rb') as f, open(loc, 'wb') as e:
        r = f.read()
        e.write(r)


if __name__ == '__main__':
    get_data('img.PNG')
    # p.revert()
    # p.hide_data("Hello my name is Sid")
    # r = p.read_data()
    # print(r)

