from keras.models import load_model
import numpy as np 
import io
import base64
import pandas as pd 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
import os
model_path = os.path.join(os.path.dirname(__file__), '../models/modelfuture.h5')
from keras.layers import Dense,LSTM,Dropout
from multiprocessing import Process
import matplotlib.dates as mdates
from datetime import datetime, timedelta


# Load the model
def company_stock_predict(df):
    model = load_model(model_path)
    sc = MinMaxScaler(feature_range=(0,1))
    testData = df
    # testData["Close"]=pd.to_numeric(testData.Close,errors='coerce')
    # testData = testData.dropna()
    # testData = testData.iloc[:,4:5]
    # sc.fit_transform(testData)
    # y_test = testData.iloc[60:,0:].values 
    # #input array for the model
    # inputClosing = testData.iloc[:,0:].values
    # inputClosing
    # inputClosing_scaled = sc.transform(inputClosing)
    # X_test = []
    # length = len(testData)
    # timestep = 60
    # for i in range(timestep,length):  
    #     X_test.append(inputClosing_scaled[i-timestep:i,0])
    # X_test = np.array(X_test)
    # X_test = np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
    # y_pred = model.predict(X_test)
    # predicted_price = sc.inverse_transform(y_pred)
    # plt.clf() 
    # # plt.plot(y_test, color = 'red', label = 'Actual Stock Price')
    # plt.plot(predicted_price, color = 'green', label = 'Predicted Stock Price')
    # plt.title('Stock prediction')
    # plt.xlabel('Time')
    # plt.ylabel('Stock Price')
    # plt.legend()
    print(df["Date"])
    testData=df.reset_index()['Close']
    print(testData)
    # print(temp)
    testData=sc.fit_transform(np.array(testData).reshape(-1,1))
    le=len(testData)
    lehun=le-100
    x_input=testData[lehun:le].reshape(1,-1)

    # print(x_input)
    temp_input=list(x_input)
    temp_input=temp_input[0].tolist()


    lst_output=[]
    n_steps=100
    i=0
    while(i<7):
        
        if(len(temp_input)>100):
            #print(temp_input)
            x_input=np.array(temp_input[1:])
            x_input=x_input.reshape(1,-1)
            x_input = x_input.reshape((1, n_steps, 1))
            #print(x_input)
            yhat = model.predict(x_input, verbose=0)
            temp_input.extend(yhat[0].tolist())
            temp_input=temp_input[1:]
            #print(temp_input)
            lst_output.extend(yhat.tolist())
            i=i+1
        else:
            x_input = x_input.reshape((1, n_steps,1))
            yhat = model.predict(x_input, verbose=0)
            temp_input.extend(yhat[0].tolist())
            lst_output.extend(yhat.tolist())
            i=i+1
    dates=df.reset_index()["Date"]
    print(dates)
    dateList=np.array(dates).reshape(-1,1)
    dateList2=dateList.tolist()
    testData2 = testData.tolist()
    testData2.extend(lst_output)
    testData2 = sc.inverse_transform(testData2).tolist()
    actual_data = testData2[:le]
    predicted_data = testData2[le:]
    print(len(actual_data))
    print(len(testData))
    print(len(testData2))
    print(len(predicted_data))
    start_date = datetime.today() - timedelta(days=len(testData))
    # print("start date ",start_date)
    # dates = [(start_date + timedelta(days=i)).strftime('%d %m %Y') for i in range(len(actual_data))]
    # print(dates)

    plt.clf() 
    # plt.plot(actual_data, color='green', label='Actual Stock Price')
    # plt.plot(range(len(actual_data), len(testData2)), predicted_data, color='red', label='Predicted Stock Price')
    plt.plot(testData2)
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.title('Stock prediction')
    plt.legend()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    

    plot_url = base64.b64encode(img.getvalue()).decode()

    # p = Process(target=generate_plot, args=(y_test, predicted_price))
    # p.start()
    # p.join()
    
    return plot_url

