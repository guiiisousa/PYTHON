import yfinance as yf

import time

def Get_history(ticket): 
    
    fiis = [f"{ticket}"]
            
    dados = {}

    for fii in fiis:
        dados[fii] = yf.Ticker(f"{ticket}").history(period="1wk")
        time.sleep(1)

    return print(dados[f"{ticket}"].tail())

    
