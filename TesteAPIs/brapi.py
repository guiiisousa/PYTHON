# from brapi import *

# def Get_Dividend(ticket):
#     client = Brapi(api_key='itcS4pRnngioRjSRooCZQi')
#     quotes = client.quote.retrieve(
#         tickers=f'{ticket - '.SA'}',
#         range='5d',
#         interval='1d',
#         fundamental=True
#     )
#     return print(quotes.results[0].regular_market_price) 
   
# print(Get_Dividend("MXRF11.SA"))

from brapi import *

def get_dividend(ticker):
    ticker_clean = ticker.removesuffix(".SA")
    
    client = Brapi(api_key="")

    quotes = client.quote.retrieve(
        tickers=ticker,
        range="5d",
        interval="1d",
        fundamental=True
    )

    result = quotes["results"][0]

    # exemplo: pegando dividend yield
    return result.get("dividendYield")

print(get_dividend("MXRF11.SA"))