import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from flask import Flask
from flask import send_file
from os import path

app = Flask(__name__)

# prevent matplotlib from opening a gui
plt.ioff()
mpl.use('Agg')


@app.route('/')
def hello_world():
    # data_source = np.random.randint(1, 6, 40).reshape(10, 4)
    data_source = []

    # lekerdezzuk az aktualis mappat
    current_path = path.dirname(__file__)
    print(current_path)
    file_name = 'income.txt'

    # betöltjük az adatokat, soronként
    f = open(path.join(current_path, file_name), 'r')
    lines = f.readlines()
    no_of_lines = 0
    fejlec = []

    # konverzió és beöltés data_source-ba soronként
    for line in lines:
        line = line.strip()
        line2 = line.split(", ")

        line_item_updated = ""
        line3 = []

        # kiszedjük a space-t majd int-é alakítva összefűzzük
        for line_item in line2:

            if no_of_lines > 0:
                line_item_updated = line_item.replace(" ", "")
                line3.append(int(line_item_updated))
                # betöltjük a data_source-ba, kivéve első sor / fejlécek
                data_source.append(line3)
            else:
                line3.append(line_item)
                fejlec = line3
        no_of_lines = +1
    f.close()

    print(fejlec[0])

    df = pd.DataFrame(data_source)
    df.columns = [fejlec[0], fejlec[1], fejlec[2], fejlec[3]]
    sns_plot = sns.barplot(palette="ch:.25", data=df, ci=None)
    sns_plot.figure.savefig("output.png")
    plt.close()
    return send_file('output.png', mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
