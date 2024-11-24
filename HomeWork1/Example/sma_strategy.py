from alt_backtest import strategy, position

from config import sma_period
from sma_indicator import SimpleMovingAverage

amount = 60
class SMAStrategy(strategy.Strategy):
    def __init__(self):
        super().__init__()
        self.long = SimpleMovingAverage(period=20)
        self.short = SimpleMovingAverage(period=3)

    def next(self):
        
        
        if not self.long.is_ready():
            return
        
        if not self.in_position():
            if self.get_price() > self.long.sma[0]:
                self.send_market_order_buy(amount)
                self.position_status = position.Position.long
                return
            elif self.get_price() < self.long.sma[0]:
                self.send_market_order_sell(amount)
                self.position_status = position.Position.short
            return

        if self.position_status == position.Position.long:
            if self.get_price() < self.long.sma[0]:
                self.send_market_order_sell(amount)
                self.position_status = position.Position.none
                return
        if self.position_status == position.Position.short:
            if self.get_price() > self.long.sma[0]:
                self.send_market_order_buy(amount)
                self.position_status = position.Position.none