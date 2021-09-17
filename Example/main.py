from piencrypt import pie

r = pie.PiEncrypt('pic.png')

r.get_data()

r.hide_data("Hello my name sid")

read = r.read_data()
print(read)

r.revert()