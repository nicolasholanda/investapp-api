import os
from datetime import timedelta

# Alpha Vantage Constants

# TODO: Change to real Bovespa symbol
BOVESPA_SYMBOL = 'IBM'

AV_ERROR_KEY = 'Error Message'

AV_OUTPUT_SIZE = {
    'full': 'full',
    'compact': 'compact'
}

AV_API_KEY = os.getenv('AV_API_KEY')

AV_URL = 'https://www.alphavantage.co/query'

AV_INTRADAY_INTERVAL = {
    '5': '5min',
    '10': '10min',
    '15': '15min',
    '30': '30min',
    '60': '60min'
}

AV_TIME_SERIES = {
    'intraday': 'TIME_SERIES_INTRADAY',
    'daily': 'TIME_SERIES_DAILY',
    'weekly': 'TIME_SERIES_WEEKLY',
    'monthly': 'TIME_SERIES_MONTHLY'
}

AV_TIME_SERIES_KEYS = {
    'open': '1. open',
    'high': '2. high',
    'low': '3. low',
    'close': '4. close',
    'volume': '5. volume'
}

AV_TIME_SERIES_METADATA = {
    'symbol': '2. Symbol',
    'last_refreshed': '3. Last Refreshed'
}


# InvestApp Constants

IA_INTERVAL = {
    '1D': {
        'function': AV_TIME_SERIES['intraday'],
        'interval': AV_INTRADAY_INTERVAL['5'],
        'timedelta': timedelta(days=1),
        'date_regex': '%Y-%m-%d %H:%M:%S'
    },
    '5D': {
        'function': AV_TIME_SERIES['intraday'],
        'interval': AV_INTRADAY_INTERVAL['30'],
        'timedelta': timedelta(days=5),
        'date_regex': '%Y-%m-%d %H:%M:%S'
    },
    '1M': {
        'function': AV_TIME_SERIES['daily'],
        'timedelta': timedelta(days=30),
        'date_regex': '%Y-%m-%d'
    },
    '6M': {
        'function': AV_TIME_SERIES['daily'],
        'timedelta': timedelta(days=30*6),
        'date_regex': '%Y-%m-%d'
    },
    '1Y': {
        'function': AV_TIME_SERIES['daily'],
        'timedelta': timedelta(days=30*12),
        'date_regex': '%Y-%m-%d'
    },
    '5Y': {
        'function': AV_TIME_SERIES['monthly'],
        'timedelta': timedelta(days=30*12*5),
        'date_regex': '%Y-%m-%d'
    }
}
