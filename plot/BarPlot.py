import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def drawPlot():
    Y = pd.read_csv('https://raw.githubusercontent.com/pdanh2682000/Crime_KKDL_DoAn/main/Colab/Y_crime.csv')

    classPredict = [Y.value_counts()[0], Y.value_counts()[1]]
    classLabel =  ['False', 'True']

    plt.bar(classLabel, classPredict)

    plt.savefig('./static/BarPlot.png')