import requests
from werkzeug.exceptions import BadRequest, TooManyRequests

from investapp.models.chart_time_series import ChartTimeSeries
from investapp.models.global_quote import GlobalQuote
from investapp.models.global_quote_search import GlobalQuoteSearch
from investapp.models.symbol_search import SymbolSearch
from investapp.models.time_series_search import TimeSeriesSearch
from investapp.utils import constants, alpha_vantage_utils
from investapp.utils.constants import AV_GLOBAL_QUOTE_ROOT_KEY, AV_SYMBOL_SEARCH_ROOT_KEY


def get_time_series(search: TimeSeriesSearch) -> ChartTimeSeries:
    """
    Método responsável por buscar série temporal de pontos por empresa, considerando os filtros recebidos
    por parâmetro
    :param search: Filtros da busca
    :return: Objeto contendo toda a série temporal de pontos da empresa
    """

    response: dict = requests.get(constants.AV_URL, params=search.json()).json()
    if response.get(constants.AV_ERROR_KEY):
        raise BadRequest('Erro ao requisitar série temporal na API da Alpha Vantage. Verifique os parâmetros enviados.')
    elif response.get(constants.AV_NOTE_KEY):
        raise TooManyRequests('Muitas requisições ao servidor.')
    return alpha_vantage_utils.to_chart_time_series(response, search.timedelta, search.date_regex)


def get_global_quote(search: GlobalQuoteSearch) -> GlobalQuote:
    """
    Método responsável por buscar cotação global por empresa, considerando o símbolo recebido
    por parâmetro
    :param search: Parâmetros da empresa reconhecida pelo Alpha Vantage
    :return: Objeto contendo a cotação atual da empresa
    """

    response: dict = requests.get(constants.AV_URL, params=search.json()).json()
    if response.get(constants.AV_NOTE_KEY):
        raise TooManyRequests('Muitas requisições ao servidor.')

    global_quote_json: dict = response.get(AV_GLOBAL_QUOTE_ROOT_KEY)

    if not global_quote_json:
        raise BadRequest('Cotação global vazia. Verifique os parâmetros enviados.')

    return alpha_vantage_utils.to_global_quote(global_quote_json)


def search_company(search: SymbolSearch):
    """
    Método responsável por buscar símbolos de empresas, considerando a palavra-chave recebida
    por parâmetro
    :param search: Parâmetros para buscar o símbolo da empresa no Alpha Vantage
    :return: Objeto contendo todas as empresas cujo símbolo coincide com a palavra-chave enviada.
    """

    response: dict = requests.get(constants.AV_URL, params=search.json()).json()
    if response.get(constants.AV_NOTE_KEY):
        raise TooManyRequests('Muitas requisições ao servidor.')

    result_search_json: dict = response.get(AV_SYMBOL_SEARCH_ROOT_KEY)

    return alpha_vantage_utils.to_search_result(result_search_json)
