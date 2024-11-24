from alt_backtest import start
from config import start_cash,data__path, start_date,end_date, format_date
from sma_strategy import SMAStrategy
import os
print(os.getcwd())
start.run(SMAStrategy, start_cash,data__path,start_date,end_date, format_date)