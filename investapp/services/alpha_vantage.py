import requests
from werkzeug.exceptions import BadRequest

from investapp.models.chart_time_series import ChartTimeSeries
from investapp.models.time_series_search import TimeSeriesSearch
from investapp.utils import constants, alpha_vantage_utils


def get_time_series(search: TimeSeriesSearch) -> ChartTimeSeries:
    """
    Método responsável por buscar série temporal de pontos por empresa, considerando os filtros recebidos
    por parâmetro
    :param search: Filtros da busca
    :return: Objeto contendo toda a série temporal de pontos da empresa
    """

    response = requests.get(constants.AV_URL, params=search.json()).json()
    if response.get(constants.AV_ERROR_KEY):
        raise BadRequest('Erro ao requisitar série temporal na API da Alpha Vantage. Verifique os parâmetros enviados.')
    return alpha_vantage_utils.to_chart_time_series(response, search.timedelta, search.date_regex)
