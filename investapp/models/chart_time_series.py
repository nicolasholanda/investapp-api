class ChartTimeSeriesItem:
    def __init__(self, close: float, timestamp: float):
        self.close = close
        self.timestamp = timestamp

    def json(self) -> dict:
        """
        Método resposável por converter o objeto da classe ChartTimeSeriesItem em uma representação JSON para ser
        retornado nas requisições.
        :return: Uma representação do objeto em JSON.
        """
        return {
            'close': self.close,
            'timestamp': self.timestamp
        }


class ChartTimeSeries:
    """
    Classe que armazena apenas informações necessárias para a geração de um gráfico.
    """
    def __init__(self, items: list,
                 last_refreshed: float,
                 symbol: str,
                 high_val: float,
                 low_val: float,
                 open_val: float):
        self.items = items
        self.symbol = symbol
        self.high = high_val
        self.low = low_val
        self.open = open_val
        self.last_refreshed = last_refreshed

    def json(self) -> dict:
        """
        Método resposável por converter o objeto da classe ChartTimeSeries em uma representação JSON para ser
        retornado nas requisições.
        :return: Uma representação do objeto em JSON.
        """
        return {
            'low': self.low,
            'open': self.open,
            'high': self.high,
            'symbol': self.symbol,
            'last_refreshed': self.last_refreshed,
            'items': list(map(lambda item: item.json(), self.items))
        }
