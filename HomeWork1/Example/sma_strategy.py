from alt_backtest import strategy, position

from config import sma_period
from sma_indicator import SimpleMovingAverage

koeff = 0.99
class SMAStrategy(strategy.Strategy):
    def __init__(self):
        super().__init__()
        self.long = SimpleMovingAverage(period=20)
        self.short = SimpleMovingAverage(period=3)
        self.last_order = None
        self.amount = 0
        
        
    def next(self):
        print(f"balance {self.get_current_balance()}, bought {self.amount}")
        
        if not self.long.is_ready():
            return
        
        if not self.in_position():
            self.amount = self.get_current_balance() * koeff // self.get_price()
            if self.get_price() > self.long.sma[0]:
                self.last_order = self.send_market_order_buy(self.amount)
                self.position_status = position.Position.long
                return
            elif self.get_price() < self.long.sma[0]:
                self.send_market_order_sell(self.amount)
                self.position_status = position.Position.short
            return
        #print(self.last_order)
        
        if self.position_status == position.Position.long:
            if self.get_price() < self.long.sma[0]:
                self.send_market_order_sell(self.amount)
                self.position_status = position.Position.none
                self.amount = 0
                return
        if self.position_status == position.Position.short:
            if self.get_price() > self.long.sma[0]:
                self.last_order = self.send_market_order_buy(self.amount)
                self.position_status = position.Position.none
                self.amount = 0
        