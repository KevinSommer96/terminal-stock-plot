import plotext as plx
from matplotlib.dates import drange
import yfinance as yf
from datetime import datetime, timedelta
import argparse 

def main():
    parser = argparse.ArgumentParser()

    # adding the arguments
    parser.add_argument("-e", default=datetime.today().isoformat(timespec='hours')[:-3])
    parser.add_argument("-t", default='1y')
    parser.add_argument("-i", default='^GDAXI')


    # Parse and print the results
    args = parser.parse_args()
    print(args)

    # compute timeframe
    if args.t == '1y': 
        timeframe = timedelta(days=365)
    elif args.t == '5y': 
        timeframe = timedelta(days=365 * 5)
    elif args.t == '10y': 
        timeframe = timedelta(days=365 * 10)
    elif args.t == '6m': 
        timeframe = timedelta(days=30 * 6)            
    elif args.t == '3m': 
        timeframe = timedelta(days=30 * 3)
    elif args.t == '1m': 
        timeframe = timedelta(days=30)
    else: 
        timeframe = timedelta(days=365)
    
        


    tickerSymbol = args.i
    end = args.e
    start = (datetime.fromisoformat(end) - timeframe).isoformat(timespec='hours')[:-3]

    # getting the financial data from yfinance
    tickerData = yf.Ticker(tickerSymbol)

    # selecting the correct timeperiod
    tickerDf = tickerData.history(period='1s', start=start, end=end)

    start = datetime.fromisoformat(start)
    end = datetime.fromisoformat(end)

    # plotting the data green if overall close goes up and red if down
    if tickerDf.iloc[0]['Close'] < tickerDf.iloc[-1]['Close']: 
        plx.plot(drange(start, end, timedelta(days=1)), tickerDf['Close'], line_color='green')
    else: 
        plx.plot(drange(start, end, timedelta(days=1)), tickerDf['Close'], line_color='red')

    plx.show()



if __name__ == '__main__':
    main()