import matplotlib.pyplot as plt


def bar():
    return Bar() 

class Plot:
    def __init__(self):
        self.chart = None


class Bar(Plot):
    def show(self):
        fig, ax = plt.subplots()

        category_name = self.chart.binds['category']
        categories = self.chart.data.groupby([category_name]).count()
        categories = self.chart.data.groupby([category_name]).size().reset_index(name='count')

        cat = categories[category_name]
        counts = categories['count']
        # bar_labels = ['red', 'blue', '_red', 'orange']
        # bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

        ax.bar(cat, counts)
        # ax.bar(cat, counts, label=bar_labels, color=bar_colors)

        plt.show()
        print('bar plot')