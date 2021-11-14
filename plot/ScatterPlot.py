import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

def drawPlot():
    attrib = pd.read_csv('https://raw.githubusercontent.com/pdanh2682000/Crime_KKDL_DoAn/main/Colab/attributes.csv', delim_whitespace = True)
    data = pd.read_csv('https://raw.githubusercontent.com/pdanh2682000/Crime_KKDL_DoAn/main/Colab/communities.data', names = attrib['attributes'])

    sns.pairplot(data[['agePct12t21', 'agePct12t29', 'agePct16t24', 'agePct65up']])
    # plt.show()

    plt.savefig('./static/ScatterPlot.png')