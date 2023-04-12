class Environment:
    # PRICE_IDX = 4  # 종가의 위치
    PRICE_IDX = 3  # 환율
    BUY_PRICE_IDX = 1  # 매입가
    SELL_PRICE_IDX = 2  # 매도가

    def __init__(self, chart_data=None):
        self.chart_data = chart_data
        self.observation = None
        self.idx = -1

    def reset(self):
        self.observation = None
        self.idx = -1

    def observe(self):
        if len(self.chart_data) > self.idx + 1:
            self.idx += 1
            self.observation = self.chart_data.iloc[self.idx]
            return self.observation
        return None

    def get_price(self):
        if self.observation is not None:
            return self.observation[self.PRICE_IDX]
        return None
    
    def get_buy_price(self):
        if self.observation is not None:
            return self.observation[self.BUY_PRICE_IDX]
        return None
    
    def get_sell_price(self):
        if self.observation is not None:
            return self.observation[self.SELL_PRICE_IDX]
        return None