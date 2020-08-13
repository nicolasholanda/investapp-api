from datetime import datetime
from .constants import AV_TIME_SERIES_KEYS, AV_TIME_SERIES_METADATA
from ..models.chart_time_series import ChartTimeSeries, ChartTimeSeriesItem


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
