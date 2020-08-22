from datetime import datetime
from .constants import AV_TIME_SERIES_KEYS, AV_TIME_SERIES_METADATA, AV_GLOBAL_QUOTE_KEYS, AV_SYMBOL_SEARCH_KEYS, \
    AV_OVERVIEW_KEYS
from ..models.chart_time_series import ChartTimeSeries, ChartTimeSeriesItem
from ..models.company_overview import CompanyOverview
from ..models.global_quote import GlobalQuote
from ..models.search_result import SearchResult, SearchResultItem


def to_chart_time_series(full_series: dict, timedelta, date_regex: str) -> ChartTimeSeries:
    """
    Método responsável por converter a resposta JSON vinda da Alpha Vantage em um objeto contendo apenas
    informações necessárias para o gráfico.
    :param date_regex: Regex para comparar as datas no objeto time_series
    :param timedelta: Período em que os registros devem estar.
    :param full_series: Resposta JSON da Alpha Vantage
    :return: Objeto ChartTimeSeries contendo informações necessárias para gerar um gráfico
    """

    full_object_keys: list = list(full_series.keys())
    meta_data: dict = full_series.get(full_object_keys[0])
    time_series: dict = full_series.get(full_object_keys[1])

    last_refreshed: str = meta_data.get(AV_TIME_SERIES_METADATA['last_refreshed'])
    last_refreshed_date: datetime = datetime.strptime(last_refreshed, date_regex)

    time_series_list: list = []
    for key, value in time_series.items():
        date: datetime = datetime.strptime(key, date_regex)
        if (last_refreshed_date - date) <= timedelta:
            close: float = float(value.get(AV_TIME_SERIES_KEYS['close']))
            time_series_list.append(ChartTimeSeriesItem(close, date.timestamp() * 1000))
        else:
            break

    return ChartTimeSeries(time_series_list)


def to_global_quote(full_global_quote: dict) -> GlobalQuote:
    """
    Método responsável por converter o JSON da cotação global em um objeto GlobalQuote.
    :param full_global_quote: Resposta original retornada pelo servidor
    :return: Objeto GlobalQuote
    """

    symbol: str = full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['symbol'])
    open_val: float = float(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['open']))
    high_val: float = float(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['high']))
    low_val: float = float(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['low']))
    price: float = float(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['price']))
    volume: int = int(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['volume']))
    latest_trading_day: float = datetime.strptime(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['latest_trading_day']),
                                           '%Y-%m-%d').timestamp() * 1000
    previous_close = float(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['previous_close']))
    change = float(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['change']))
    change_percent = full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['change_percent'])

    return GlobalQuote(symbol, open_val, high_val, low_val, price, volume, latest_trading_day, previous_close,
                       change, change_percent)


def to_search_result(full_search_result: dict) -> SearchResult:
    """
    Método responsável por converter o JSON do resultado da busca por símbolo em um objeto SearchResult.
    :param full_search_result: Resposta original retornada pelo servidor
    :return: Objeto SearchResult
    """
    search_items: list = []

    for result in full_search_result:
        symbol: str = result.get(AV_SYMBOL_SEARCH_KEYS['symbol'])
        name: str = result.get(AV_SYMBOL_SEARCH_KEYS['name'])
        type_val: str = result.get(AV_SYMBOL_SEARCH_KEYS['type'])
        region: str = result.get(AV_SYMBOL_SEARCH_KEYS['region'])
        market_open: str = result.get(AV_SYMBOL_SEARCH_KEYS['market_open'])
        market_close: str = result.get(AV_SYMBOL_SEARCH_KEYS['market_close'])
        timezone: str = result.get(AV_SYMBOL_SEARCH_KEYS['timezone'])
        currency: str = result.get(AV_SYMBOL_SEARCH_KEYS['currency'])
        match_score: str = result.get(AV_SYMBOL_SEARCH_KEYS['match_score'])

        search_items.append(SearchResultItem(symbol, name, type_val, region, market_open, market_close, timezone,
                                             currency, match_score))

    return SearchResult(search_items)


def to_company_overview(full_company_overview: dict) -> CompanyOverview:
    """
    Método responsável por converter o JSON do resultado da visão geral da empresa em um objeto CompanyOverview.
    :param full_company_overview: Resposta original retornada pelo servidor
    :return: Objeto CompanyOverview
    """
    symbol = full_company_overview.get(AV_OVERVIEW_KEYS.get('symbol'))
    name = full_company_overview.get(AV_OVERVIEW_KEYS.get('name'))
    description = full_company_overview.get(AV_OVERVIEW_KEYS.get('description'))
    exchange = full_company_overview.get(AV_OVERVIEW_KEYS.get('exchange'))
    currency = full_company_overview.get(AV_OVERVIEW_KEYS.get('currency'))
    country = full_company_overview.get(AV_OVERVIEW_KEYS.get('country'))
    sector = full_company_overview.get(AV_OVERVIEW_KEYS.get('sector'))
    industry = full_company_overview.get(AV_OVERVIEW_KEYS.get('industry'))
    address = full_company_overview.get(AV_OVERVIEW_KEYS.get('address'))

    return CompanyOverview(symbol, name, description, exchange, currency, country, sector, industry, address)
