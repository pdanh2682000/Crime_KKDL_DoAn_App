import pandas as pd
import numpy as np 
from sklearn.naive_bayes import GaussianNB

X = pd.read_csv('https://raw.githubusercontent.com/pdanh2682000/Crime_KKDL_DoAn/main/Colab/X_crime.csv')
Y = pd.read_csv('https://raw.githubusercontent.com/pdanh2682000/Crime_KKDL_DoAn/main/Colab/Y_crime.csv')

# print(X.head())
# print(Y.head())

G_Naive_Bayes = GaussianNB()
G_Naive_Bayes.fit(X, Y)

def classify(a, b, c, d, e, f, g, h, i, j):
    arr = np.array([a, b, c, d, e, f, g, h, i, j]) # Convert to numpy array
    arr = arr.astype(np.float64) # Change the data type to float
    query = arr.reshape(1, -1) # 
    prediction = G_Naive_Bayes.predict(query)
    return prediction # Return the prediction

# print(classify(0.47,0.24,0.43,0.74,0.6,0.45,0.39,0.91,0.29,1.0))
