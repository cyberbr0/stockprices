import yfinance as yf
import time

tickers = ['AAPL', 'BRK-A', 'META', 'MSFT', 'NVDA', 'TSLA'] 
interval_minutes = 15

while True:
    stock_data = {}
    
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d')
        stock_data[ticker] = data    
        
    for ticker, data in stock_data.items():
        print(f'\n\nApple Inc | AAPL:',stock_data['AAPL'],'\n\n\n')
        print(f'Berkshire Hathaway Inc Class A |BRK-A:',stock_data['BRK-A'],'\n\n\n')
        print(f'Meta Platforms Inc | META:',stock_data['META'],'\n\n\n')
        print(f'Microsoft Corp | MSFT:',stock_data['MSFT'],'\n\n\n')
        print(f'Nvidia Corp | NVDA:',stock_data['NVDA'],'\n\n\n')
        print(f'Tesla Inc | TSLA:', stock_data['TSLA'],'\n\n\n')

        #time.sleep(interval_minutes * 15)  #Can use this syntax to control sleep intervals
    