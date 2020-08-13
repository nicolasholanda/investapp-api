from investapp.utils import constants
from investapp.utils.constants import IA_INTERVAL


class TimeSeriesSearch:
    """
    Classe que representa o filtro de busca de séries temporais
    """

    def __init__(self, params: dict):
        ia_interval = IA_INTERVAL.get(params.get('interval', list(IA_INTERVAL.keys())[0]))
        self.apikey = constants.AV_API_KEY
        self.interval = ia_interval.get('interval')
        self.timedelta = ia_interval.get('timedelta')
        self.symbol = params.get('symbol', constants.BOVESPA_SYMBOL)
        self.function = ia_interval.get('function')
        self.outputsize = ia_interval.get('outputsize')
        self.date_regex = ia_interval.get('date_regex')

    def json(self):
        """
        Método resposável por converter o objeto da classe TimeSeriesSearch em uma representação JSON para ser
        enviado nas requisições.
        :return: Uma representação do objeto em JSON.
        """
        result = {
            'function': self.function,
            'apikey': self.apikey,
            'outputsize': self.outputsize,
            'symbol': self.symbol,
        }

        if self.interval is not None:
            result['interval'] = self.interval

        return result
