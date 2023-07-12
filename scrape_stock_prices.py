import yfinance as yf
from datetime import datetime

tickers = ['AAPL','BRK-A','META','MSFT','NVDA','TSLA'] 
interval_minutes = 15
now = datetime.now()

stock_data = {}

for ticker in tickers:
    
    stock = yf.Ticker(ticker)
    data = yf.download(ticker, start='2023-07-10', end=now.strftime('%Y-%m-%d'))
    stock_data[ticker] = data    

print('Stock Prices for APL, BRK-A, META, MSFT, NVDA, and TSLA\n\n')
print('Apple Inc | AAPL:',stock_data['AAPL'],'\n\n')
print('Berkshire Hathaway Inc Class A | BRK-A:',stock_data['BRK-A'],'\n\n')
print('Meta Platforms Inc | META:',stock_data['META'],'\n\n')
print('Microsoft Corp | MSFT:',stock_data['MSFT'],'\n\n')
print('Nvidia Corp | NVDA:',stock_data['NVDA'],'\n\n')
print('Tesla Inc | TSLA:', stock_data['TSLA'],'\n\n')
