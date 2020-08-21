class SearchResultItem:
    """
    Classe que armazena o resultado individual da busca por empresas no Alpha Vantage
    """
    def __init__(self, symbol: str, name: str, type_val: str, region: str, market_open: str, market_close: str,
                 timezone: str, currency: str, match_score: str):
        self.symbol = symbol
        self.name = name
        self.type = type_val
        self.region = region
        self.market_close = market_close
        self.market_open = market_open
        self.timezone = timezone
        self.currency = currency
        self.match_score = match_score

    def json(self) -> dict:
        """
        Método resposável por converter o objeto da classe ChartTimeSeries em uma representação JSON para ser
        retornado nas requisições.
        :return: Uma representação do objeto em JSON.
        """
        return {
            'symbol': self.symbol,
            'name': self.name,
            'type': self.type,
            'region': self.region,
            'market_open': self.market_open,
            'market_close': self.market_close,
            'timezone': self.timezone,
            'currency': self.currency,
            'match_score': self.match_score
        }


class SearchResult:
    """
    Classe que armazena todos os resultados da busca por empresas no Alpha Vantage
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
