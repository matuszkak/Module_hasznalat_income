from os import path

# lekerdezzuk az aktualis mappat
current_path = path.dirname(__file__)
print(current_path)
file_name = 'income.txt'

data_source = []
f = open(path.join(current_path, file_name), 'r')

lines = f.readlines()
no_of_lines = 0
for line in lines:

    line = line.strip()
    line2 = line.split(", ")

    line_item_updated = ""
    line3 = []
    if no_of_lines > 0:
        for line_item in line2:
            line_item_updated = line_item.replace(" ", "")

            line3.append(int(line_item_updated))

        data_source.append(line3)  #
    no_of_lines = +1
f.close()
