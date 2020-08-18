class GlobalQuote:
    """
    Classe que armazena cotação global por empresa.
    """
    def __init__(self, symbol: str, open_val: float, high_val: float, low_val: float, price: float, volume: int,
                 latest_trading_day: float, previous_close: float, change: float, change_percent: str):
        self.low = low_val
        self.price = price
        self.symbol = symbol
        self.open = open_val
        self.high = high_val
        self.change = change
        self.volume = volume
        self.previous_close = previous_close
        self.change_percent = change_percent
        self.latest_trading_day = latest_trading_day

    def json(self) -> dict:
        """
        Método resposável por converter o objeto da classe GlobalQuote em uma representação JSON para ser
        retornado nas requisições.
        :return: Uma representação do objeto em JSON.
        """
        return {
            'low': self.low,
            'price': self.price,
            'symbol': self.symbol,
            'open': self.open,
            'high': self.high,
            'change': self.change,
            'volume': self.volume,
            'previous_close': self.previous_close,
            'change_percent': self.change_percent,
            'latest_trading_day': self.latest_trading_day
        }
