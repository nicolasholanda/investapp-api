from investapp.utils.constants import AV_API_KEY, AV_TIME_SERIES


class GlobalQuoteSearch:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.apikey = AV_API_KEY
        self.function = AV_TIME_SERIES['global']

    def json(self):
        return {
            'apikey': self.apikey,
            'function': self.function,
            'symbol': self.symbol
        }
