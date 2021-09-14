def get_binary():
    with open('sidlogo.jpg', 'rb') as f, open('binary.txt', 'wb') as b:
        r = f.read()
        b.write(r)

def process_pic():
    with open('binary.txt', 'rb') as f, open('new.jpg', 'wb') as e:
        r = f.read()
        e.write(r)


def hide_data():
    with open('new.jpg', 'ab') as f:
        f.write(b"HEREHello World")
        

def read_data():
    with open('new.jpg', 'rb') as f:
        content = f.read()
        # offset = content.index(bytes.fromhex('FFD9'))

        # f.seek(offset + 2)
        list = content.split(b'HERE')
        # print(f.read())
        print(list[1].decode("utf-8") )


if __name__ == '__main__':
    # process_pic()
    # get_binary()
    hide_data()
    read_data()
