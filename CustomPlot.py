import matplotlib.pyplot as plt

class CustomPlot:
    def __init__(self, df = None):
        self.__df = df

    def create_plot(self, txt):
        self.__df.plot(kind=txt.lower(), legend=True)
        plt.show()