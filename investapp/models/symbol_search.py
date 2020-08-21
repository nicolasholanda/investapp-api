from investapp.utils.constants import AV_FUNCTIONS, AV_API_KEY


class SymbolSearch:
    """
    Classe que representa o filtro de busca por empresas no Alpha Vantage
    """

    def __init__(self, params: dict):
        self.keywords = params.get('keywords')
        self.apikey = AV_API_KEY
        self.function = AV_FUNCTIONS['search']

    def json(self) -> dict:
        """
        Método resposável por converter o objeto da classe ChartTimeSeries em uma representação JSON para ser
        retornado nas requisições.
        :return: Uma representação do objeto em JSON.
        """
        return {
            'apikey': self.apikey,
            'function': self.function,
            'keywords': self.keywords
        }
