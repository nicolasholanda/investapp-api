class CompanyOverview:
    """
    Classe que armazena visão geral da empresa.
    """
    def __init__(self, symbol: str, name: str, description: str, exchange: str, currency: str, country: str,
                 sector: str, industry: str, address: str):
        self.symbol = symbol
        self.name = name
        self.description = description
        self.exchange = exchange
        self.currency = currency
        self.country = country
        self.sector = sector
        self.industry = industry
        self.address = address

    def json(self) -> dict:
        """
        Método resposável por converter o objeto da classe GlobalQuote em uma representação JSON para ser
        retornado nas requisições.
        :return: Uma representação do objeto em JSON.
        """
        return {
            'symbol': self.symbol,
            'name': self.name,
            'description': self.description,
            'exchange': self.exchange,
            'currency': self.currency,
            'country': self.country,
            'sector': self.sector,
            'industry': self.industry,
            'address': self.address
        }
