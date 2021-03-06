from investapp.utils.constants import AV_API_KEY, AV_FUNCTIONS


class GlobalQuoteSearch:
    """
    Classe que representa o filtro de busca de cotação global por empresas.
    """
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.apikey = AV_API_KEY
        self.function = AV_FUNCTIONS['global']

    def json(self) -> dict:
        """
        Método resposável por converter o objeto da classe ChartTimeSeries em uma representação JSON para ser
        retornado nas requisições.
        :return: Uma representação do objeto em JSON.
        """
        return {
            'apikey': self.apikey,
            'function': self.function,
            'symbol': self.symbol
        }
