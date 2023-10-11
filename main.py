import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
matplotlib.use('TkAgg')


DATA = 'https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json'
FOLDER = 'plots'


def draw_plots(data, names: list[list]):

    if not os.path.exists(FOLDER):
        os.mkdir(FOLDER)

    try:
        df = pd.read_json(data, orient="records")
    except Exception as e:
        return print(f"error data -> {e}")

    for items in tqdm(names):
        plot_name = "_".join(items)
        df_cols = df[[*items]]
        fig, axs = plt.subplots(
            figsize=(12, 4),
            subplot_kw={
                "title": f"file: {plot_name}",
                "xlabel": "count",
                "ylabel": "deviation degrees",
            }
        )
        df_cols.plot.area(ax=axs)
        fig.savefig(FOLDER + "/" + plot_name)

    plots = os.listdir(FOLDER)

    return [FOLDER + "/" + str(i) for i in plots]


class Plots:
    def __init__(self):
        self.fig, self.axs = plt.subplots()

    def hist(self, item):
        item.plot.hist(ax=self.axs)
        plt.show()


if __name__ == "__main__":
    df = pd.read_json(DATA, orient="records")
    plot = Plots()
    plot_min = plot.hist(df['min'])
