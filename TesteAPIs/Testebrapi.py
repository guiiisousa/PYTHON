from brapi import *

def Get_Dividend(ticket):
    client = Brapi(api_key='itcS4pRnngioRjSRooCZQi')
    quotes = client.quote.retrieve(
        tickers=f'{ticket.removesuffix(".SA")}',
        range='5d',
        interval='1d',
        fundamental=True
    )
    return print(quotes.results[0].regular_market_price) 
   
print(Get_Dividend("MXRF11.SA"))

# from brapi import Brapi

# def get_dividend(ticker):
#     ticker_clean = ticker.removesuffix(".SA")
    
#     client = Brapi(api_key="itcS4pRnngioRjSRooCZQi")

#     quotes = client.quote.retrieve(
#         tickers=ticker_clean,
#         range="5d",
#         interval="1d",
#         fundamental=True,
#         modules = "dividends"
#     )

#     result = quotes.results[0]

#     if result:
#         ultimo = result[0]
#         return ultimo["value"]
    
#     # exemplo: pegando dividend yield
#     return None

# print(get_dividend("MXRF11.SA"))
