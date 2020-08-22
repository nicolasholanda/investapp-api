import os
from datetime import timedelta

# Alpha Vantage Constants

# TODO: Change to real Bovespa symbol
BOVESPA_SYMBOL = 'IBM'

AV_ERROR_KEY = 'Error Message'

AV_NOTE_KEY = 'Note'

AV_GLOBAL_QUOTE_ROOT_KEY = 'Global Quote'

AV_OUTPUT_SIZE = {
    'full': 'full',
    'compact': 'compact'
}

AV_API_KEY = os.getenv('AV_API_KEY', 'IRDEZH22MZ1ZY29Q')

AV_URL = 'https://www.alphavantage.co/query'

AV_INTRADAY_INTERVAL = {
    '5': '5min',
    '10': '10min',
    '15': '15min',
    '30': '30min',
    '60': '60min'
}

AV_FUNCTIONS = {
    'intraday': 'TIME_SERIES_INTRADAY',
    'daily': 'TIME_SERIES_DAILY',
    'weekly': 'TIME_SERIES_WEEKLY',
    'monthly': 'TIME_SERIES_MONTHLY',
    'global': 'GLOBAL_QUOTE',
    'search': 'SYMBOL_SEARCH',
    'overview': 'OVERVIEW'
}

AV_TIME_SERIES_KEYS = {
    'open': '1. open',
    'high': '2. high',
    'low': '3. low',
    'close': '4. close',
    'volume': '5. volume'
}

AV_GLOBAL_QUOTE_KEYS = {
    'symbol': '01. symbol',
    'open': '02. open',
    'high': '03. high',
    'low': '04. low',
    'price': '05. price',
    'volume': '06. volume',
    'latest_trading_day': '07. latest trading day',
    'previous_close': '08. previous close',
    'change': '09. change',
    'change_percent': '10. change percent'
}

AV_TIME_SERIES_METADATA = {
    'symbol': '2. Symbol',
    'last_refreshed': '3. Last Refreshed'
}

AV_SYMBOL_SEARCH_ROOT_KEY = 'bestMatches'

AV_SYMBOL_SEARCH_KEYS = {
    'symbol': '1. symbol',
    'name': '2. name',
    'type': '3. type',
    'region': '4. region',
    'market_open': '5. marketOpen',
    'market_close': '6. marketClose',
    'timezone': '7. timezone',
    'currency': '8. currency',
    'match_score': '9. matchScore',
}

AV_OVERVIEW_KEYS = {
    'symbol': 'Symbol',
    'name': 'Name',
    'description': 'Description',
    'exchange': 'Exchange',
    'currency': 'Currency',
    'country': 'Country',
    'sector': 'Sector',
    'industry': 'Industry',
    'address': 'Address'
}


# InvestApp Constants

IA_INTERVAL = {
    '1D': {
        'function': AV_FUNCTIONS['intraday'],
        'interval': AV_INTRADAY_INTERVAL['5'],
        'timedelta': timedelta(days=1),
        'date_regex': '%Y-%m-%d %H:%M:%S'
    },
    '5D': {
        'function': AV_FUNCTIONS['intraday'],
        'interval': AV_INTRADAY_INTERVAL['30'],
        'timedelta': timedelta(days=5),
        'date_regex': '%Y-%m-%d %H:%M:%S'
    },
    '1M': {
        'function': AV_FUNCTIONS['daily'],
        'timedelta': timedelta(days=30),
        'date_regex': '%Y-%m-%d'
    },
    '6M': {
        'function': AV_FUNCTIONS['daily'],
        'timedelta': timedelta(days=30*6),
        'date_regex': '%Y-%m-%d'
    },
    '1Y': {
        'function': AV_FUNCTIONS['daily'],
        'timedelta': timedelta(days=30*12),
        'date_regex': '%Y-%m-%d'
    },
    '5Y': {
        'function': AV_FUNCTIONS['monthly'],
        'timedelta': timedelta(days=30*12*5),
        'date_regex': '%Y-%m-%d'
    }
}
