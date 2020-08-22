from investapp.utils.constants import AV_API_KEY, AV_FUNCTIONS


class OverviewSearch:
    """
    Classe que representa o filtro de busca de visão geral por empresas.
    """

    def __init__(self, params: dict):
        self.symbol = params.get('symbol')
        self.apikey = AV_API_KEY
        self.function = AV_FUNCTIONS['overview']

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
