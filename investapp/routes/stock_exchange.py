from flask import Blueprint, request

from investapp.models.time_series_search import TimeSeriesSearch
from investapp.services import alpha_vantage
from investapp.validations.time_series_request_schema import TimeSeriesRequestSchema

bp = Blueprint('stock_exchange', __name__, url_prefix='/stock_exchange')


@bp.route('/time_series/', methods=['GET'])
def get_stock_time_series():
    """
    Método responsável por receber e processar a requisição de série temporal com os parâmetros enviados
    :return: Lista completa da série temporal filtrada
    """

    request_dict = request.args.to_dict()
    TimeSeriesRequestSchema().load(request_dict)
    params: TimeSeriesSearch = TimeSeriesSearch(request_dict)
    return alpha_vantage.get_time_series(params).json()
