from flask import Blueprint, request

from investapp.models.global_quote_search import GlobalQuoteSearch
from investapp.models.overview_search import OverviewSearch
from investapp.models.symbol_search import SymbolSearch
from investapp.models.time_series_search import TimeSeriesSearch
from investapp.services import alpha_vantage
from investapp.validations.company_overview_schema import CompanyOverviewRequestSchema
from investapp.validations.global_quote_request_schema import GlobalQuoteRequestSchema
from investapp.validations.search_request_schema import SearchRequestSchema
from investapp.validations.time_series_request_schema import TimeSeriesRequestSchema

bp = Blueprint('stock_exchange', __name__, url_prefix='/stock_exchange')


@bp.route('/time_series/', methods=['GET'])
def get_stock_time_series():
    """
    Método responsável por receber e processar a requisição de série temporal com os parâmetros enviados
    :return: Lista completa da série temporal filtrada
    """

    request_dict: dict = request.args.to_dict()
    TimeSeriesRequestSchema().load(request_dict)
    params: TimeSeriesSearch = TimeSeriesSearch(request_dict)
    return alpha_vantage.get_time_series(params).json()


@bp.route('/global_quote/<string:symbol>', methods=['GET'])
def get_global_quote(symbol: str):
    """
    Método responsável por receber e processar a requisição da cotação global com os parâmetros enviados.
    :param symbol: Símbolo da empresa, reconhecido pelo Alpha Vantage.
    :return: Objeto JSON com informações dos valores atuais da empresa.
    """

    GlobalQuoteRequestSchema().load({'symbol': symbol})
    params: GlobalQuoteSearch = GlobalQuoteSearch(symbol)
    return alpha_vantage.get_global_quote(params).json()


@bp.route('/search/', methods=['GET'])
def symbol_search():
    """
    Método responsável por receber e processar a requisição de buscar empresas com a palavra-chave enviada.
    :param keywork: Palavra-chave para fazer a busca.
    :return: Lista de empresas cujo nome ou símbolo coincidem com a palavra-chave enviada.
    """
    request_dict: dict = request.args.to_dict()
    SearchRequestSchema().load(request_dict)
    params: SymbolSearch = SymbolSearch(request_dict)
    return alpha_vantage.search_company(params).json()


@bp.route('/overview/', methods=['GET'])
def company_overview():
    """
    Método responsável por receber e processar a requisição de buscar visão geral da empresa.
    :param symbol: Símbolo da empresa.
    :return: Visão geral da empresa.
    """
    request_dict: dict = request.args.to_dict()
    CompanyOverviewRequestSchema().load(request_dict)
    params: OverviewSearch = OverviewSearch(request_dict)
    return alpha_vantage.get_company_overview(params).json()
