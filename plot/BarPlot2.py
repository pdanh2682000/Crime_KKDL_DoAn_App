import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def drawPlot():
    attrib = pd.read_csv('https://raw.githubusercontent.com/pdanh2682000/Crime_KKDL_DoAn/main/Colab/attributes.csv', delim_whitespace = True)
    data = pd.read_csv('https://raw.githubusercontent.com/pdanh2682000/Crime_KKDL_DoAn/main/Colab/communities.data', names = attrib['attributes'])

    data.hist(column = ['ViolentCrimesPerPop'], bins = 30, color = 'red', alpha = 0.8)

    plt.savefig('./static/BarPlot2.png')