import csv
import yfinance as yf
from datetime import datetime

tickers = ['AAPL','BRK-A','META','MSFT','NVDA','TSLA'] 
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

filename = 'stock.prices.csv'

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(['Date','Open','High','Low','Close','Adj Close','Volume'])
    
for stock_data[ticker] in stock_data:
    
    print(f'Artifacts uploaded to {filename}')
