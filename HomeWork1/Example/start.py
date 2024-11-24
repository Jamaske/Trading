from alt_backtest import start
from config import start_cash,data__path, start_date,end_date, format_date
from sma_strategy import SMAStrategy
from test_strategy import Test
import os
print(os.getcwd())
start.run(Test, start_cash,data__path,start_date,end_date, format_date)