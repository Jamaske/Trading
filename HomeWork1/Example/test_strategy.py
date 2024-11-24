from alt_backtest import strategy, position

from config import sma_period



class Test(strategy.Strategy):
    def __init__(self):
        super().__init__()
        self.last_order = None
        self.amount = 0
        
        
        
    def next(self):
        print(f"balance {self.get_current_balance()}, bought {self.amount}")
        
        if not self.in_position():
            self.amount = 77
            self.last_order = self.send_market_order_buy(self.amount)
            self.position_status = position.Position.long
            return
    