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
    def __init__(self, items: list):
        self.items = items

    def json(self) -> dict:
        """
        Método resposável por converter o objeto da classe ChartTimeSeries em uma representação JSON para ser
        retornado nas requisições.
        :return: Uma representação do objeto em JSON.
        """
        return {
            'items': list(map(lambda item: item.json(), self.items))
        }
