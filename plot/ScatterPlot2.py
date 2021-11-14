import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

def drawPlot():
    X = pd.read_csv('https://raw.githubusercontent.com/pdanh2682000/Crime_KKDL_DoAn/main/Colab/X_crime.csv')

    sns.lmplot(x="PctKids2Par", y="racePctWhite", line_kws={'color': 'red'} ,data=X) 
    # plt.show()
    plt.savefig('./static/ScatterPlot2.png')