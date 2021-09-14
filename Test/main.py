from piencrypt import pie

r = pie.PiEncrypt('pic.PNG')

r.get_data()

r.hide_data("Hello my name is Sid")

read = r.read_data()

r.revert()

print(read)