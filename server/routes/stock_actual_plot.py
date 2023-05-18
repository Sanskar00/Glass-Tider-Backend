from flask import Flask, request, jsonify,Blueprint,Response
from utils.company_df import company_his_df
from utils.company_symbol import compnay_symbol
from utils.company_stock_prediction import company_stock_predict
from utils.company_info import company_info
import json

stock_actual_graph_route=Blueprint('stock_actual_graph_route',__name__)
@stock_actual_graph_route.route('/stock_actual_graph_route',methods=['post'])
def stock_plot():
    word=request.data.decode('utf-8')
    symbol=compnay_symbol(word)
    dataframe=company_his_df(symbol)
    dataframe = dataframe.iloc[::-1]
    plot_image=company_stock_predict(dataframe)
    json_data = dataframe.to_dict(orient='records')
    company_info_data=company_info(symbol)
    return {"data":json_data,"company_stock_image":plot_image,'company_info':company_info_data}