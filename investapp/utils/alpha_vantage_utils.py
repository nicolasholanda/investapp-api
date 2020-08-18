from datetime import datetime
from .constants import AV_TIME_SERIES_KEYS, AV_TIME_SERIES_METADATA, AV_GLOBAL_QUOTE_KEYS
from ..models.chart_time_series import ChartTimeSeries, ChartTimeSeriesItem
from ..models.global_quote import GlobalQuote


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

    symbol: str = meta_data.get(AV_TIME_SERIES_METADATA['symbol'])
    last_refreshed: str = meta_data.get(AV_TIME_SERIES_METADATA['last_refreshed'])
    last_refreshed_date: datetime = datetime.strptime(last_refreshed, date_regex)

    last_item = time_series.get(last_refreshed)
    high_val = last_item.get(AV_TIME_SERIES_KEYS['high'])
    low_val = last_item.get(AV_TIME_SERIES_KEYS['low'])
    open_val = last_item.get(AV_TIME_SERIES_KEYS['open'])

    time_series_list: list = []
    for key, value in time_series.items():
        date: datetime = datetime.strptime(key, date_regex)
        if (last_refreshed_date - date) <= timedelta:
            close: float = float(value.get(AV_TIME_SERIES_KEYS['close']))
            time_series_list.append(ChartTimeSeriesItem(close, date.timestamp() * 1000))
        else:
            break

    return ChartTimeSeries(time_series_list,
                           last_refreshed_date.timestamp() * 1000,
                           symbol, high_val, low_val, open_val)


def to_global_quote(full_global_quote: dict) -> GlobalQuote:
    """
    Método responsável por converter o JSON da cotação global em um objeto GlobalQuote.
    :param full_global_quote:
    :return:
    """

    symbol = full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['symbol'])
    open_val = float(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['open']))
    high_val = float(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['high']))
    low_val = float(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['low']))
    price = float(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['price']))
    volume = int(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['volume']))
    latest_trading_day = datetime.strptime(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['latest_trading_day']),
                                           '%Y-%m-%d').timestamp() * 1000
    previous_close = float(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['previous_close']))
    change = float(full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['change']))
    change_percent = full_global_quote.get(AV_GLOBAL_QUOTE_KEYS['change_percent'])

    return GlobalQuote(symbol, open_val, high_val, low_val, price, volume, latest_trading_day, previous_close,
                       change, change_percent)
