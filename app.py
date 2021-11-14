from flask import Flask, request, render_template # Import flask libraries
from flask import url_for
from model import Bayes_Crime
from plot import BarPlot
from plot import BarPlot2
from plot import ScatterPlot
from plot import ScatterPlot2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os.path

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET'])
def welcome():
    return render_template('home.html')

@app.route('/classify',methods=['POST'])
def classify_type():
    try:
        PctKids2Par = request.form['PctKids2Par']
        PctIlleg = request.form['PctIlleg'] 
        PctFam2Par = request.form['PctFam2Par'] 
        racePctWhite = request.form['racePctWhite'] 
        PctYoungKids2Par = request.form['PctYoungKids2Par'] 
        pctWInvInc = request.form['pctWInvInc']
        PctTeen2Par = request.form['PctTeen2Par'] 
        FemalePctDiv = request.form['FemalePctDiv'] 
        pctWPubAsst = request.form['pctWPubAsst'] 
        TotalPctDiv = request.form['TotalPctDiv']

        # predict
        variety_Bayes = Bayes_Crime.classify(PctKids2Par,PctIlleg,PctFam2Par,racePctWhite,PctYoungKids2Par,
                                                pctWInvInc,PctTeen2Par,FemalePctDiv,pctWPubAsst,TotalPctDiv)
        return render_template('home.html', variety_Bayes=variety_Bayes, bookmarks = 'true')
    except:
        return render_template('home.html')
        # return render_template('error.html')

# @app.route('/plot')
# def chartTest():
#     X = pd.read_csv('https://raw.githubusercontent.com/pdanh2682000/Crime_KKDL_DoAn/main/Colab/X_crime.csv')
#     lnprice=np.log(price)
#     plt.plot(lnprice)   
#     plt.savefig('./static/new_plot.png')
#     return render_template('plot.html', name = 'new_plot', url ='./static/new_plot.png')

@app.route('/plot')
def chartTest():
    try:
        if(not os.path.exists('./static/BarPlot.png')):
            BarPlot.drawPlot()
            BarPlot2.drawPlot()
            ScatterPlot.drawPlot()
            ScatterPlot2.drawPlot()
            return render_template('plot.html', name0 = 'Biểu đồ Scatter về quan hệ giữa các biến', url0 ='./static/ScatterPlot2.png' 
                                        , name1 = 'Biểu đồ cột về giá trị dự đoán mức độ tội phạm', url1 ='./static/BarPlot.png'
                                        , name2 = 'Biểu đồ cột về giá trị tỉ lệ tội phạm', url2 ='./static/BarPlot2.png'
                                        , name3 = 'Biểu đồ Scatter về quan hệ giữa các biến', url3 ='./static/ScatterPlot.png')
        else:
            return render_template('plot.html', name0 = 'Biểu đồ Scatter về quan hệ giữa các biến', url0 ='./static/ScatterPlot2.png' 
                                        , name1 = 'Biểu đồ cột về giá trị dự đoán mức độ tội phạm', url1 ='./static/BarPlot.png'
                                        , name2 = 'Biểu đồ cột về giá trị tỉ lệ tội phạm', url2 ='./static/BarPlot2.png'
                                        , name3 = 'Biểu đồ Scatter về quan hệ giữa các biến', url3 ='./static/ScatterPlot.png')
    except:
        return render_template('home.html')

# Run the Flask server
if(__name__=='__main__'):
    app.run(debug=True)