from datetime import datetime, timedelta
from http.client import OK, BAD_REQUEST, TOO_MANY_REQUESTS
from time import sleep

from flask import Response
from flask.testing import FlaskClient

from investapp.utils.constants import IA_INTERVAL, BOVESPA_SYMBOL

ROUTE_PREFIX = '/stock_exchange'
INTERVAL_OPTIONS = list(IA_INTERVAL.keys())


def test_should_return_ibovespa_points_for_all_intervals(client: FlaskClient):
    """
    Testa se a API retorna a pontuação do Ibovespa em todos os períodos disponíveis.
    :param client: API cliente para testes.
    :return:
    """
    for interval_key in INTERVAL_OPTIONS:
        interval_dict = IA_INTERVAL.get(interval_key)
        response: Response = get_time_series_by_symbol_and_interval(client,
                                                                    symbol=BOVESPA_SYMBOL,
                                                                    interval=interval_key)

        assert response.status_code == OK
        assert response.json.get('symbol') == BOVESPA_SYMBOL
        assert response_is_in_range(response, interval_dict.get('timedelta'))


def test_should_return_company_points_for_all_intervals(client: FlaskClient):
    """
    Testa se a API retorna a pontuação de outras empresas em todos os períodos disponíveis.
    :param client: API cliente para testes.
    :return:
    """
    for interval_key in INTERVAL_OPTIONS:
        interval_dict = IA_INTERVAL.get(interval_key)
        response: Response = get_time_series_by_symbol_and_interval(client, symbol='BABA', interval=interval_key)

        assert response.status_code == OK
        assert response.json.get('symbol') == 'BABA'
        assert response_is_in_range(response, interval_dict.get('timedelta'))


def test_should_fail_when_interval_is_invalid(client: FlaskClient):
    """
    Testa se a API retorna um erro quando o intervalo enviado não está em IA_INTERVAL.
    :param client: API cliente para testes.
    :return:
    """
    response: Response = get_time_series_by_symbol_and_interval(client, symbol=BOVESPA_SYMBOL, interval='78D')

    assert response.status_code == BAD_REQUEST
    assert response.json.get('code') == BAD_REQUEST
    assert response.json.get('name') == 'ValidationError'
    assert 'interval' in response.json.get('description')


def test_should_fail_when_interval_is_missing(client: FlaskClient):
    """
    Testa se a API retorna um erro quando o intervalo não é enviado.
    :param client: API cliente para testes.
    :return:
    """
    response: Response = get_time_series_by_symbol_and_interval(client, symbol=BOVESPA_SYMBOL)

    assert response.status_code == BAD_REQUEST
    assert response.json.get('code') == BAD_REQUEST
    assert response.json.get('name') == 'ValidationError'
    assert 'interval' in response.json.get('description')


def test_should_fail_when_symbol_is_invalid(client: FlaskClient):
    """
    Testa se a API retorna um erro quando o símbolo enviado é invalido.
    :param client: API cliente para testes.
    :return:
    """
    response: Response = get_time_series_by_symbol_and_interval(client, symbol='9X9Y9Z',
                                                                interval=INTERVAL_OPTIONS[0])

    assert response.status_code == BAD_REQUEST
    assert response.json.get('code') == BAD_REQUEST
    assert response.json.get('name') == 'BadRequest'
    assert 'parâmetros enviados' in response.json.get('description')


def test_should_fail_when_many_requests_are_made(client: FlaskClient):
    """
    Testa se a API retorna um erro quando mais do ques 5 requisições são feitas dentro de 1 minuto.
    :param client: API cliente para testes.
    :return:
    """
    while True:
        response = client.get(f'{ROUTE_PREFIX}/time_series/', query_string={'interval': '5Y'})
        if response.status_code != OK:
            break

    assert response.json.get('code') == TOO_MANY_REQUESTS
    assert 'Muitas requisições' in response.json.get('description')


def get_time_series_by_symbol_and_interval(client: FlaskClient, **kwargs) -> Response:
    """
    Retorna a série temporal de pontos por empresa, dentro de um intervalo, e garante que o servidor não retorne
    uma exceção do tipo TooManyRequests.
    :param client: API cliente para testes.
    :key interval: Intervalo da série temporal.
    :key symbol: Símbolo da empresa desejada.
    :return: Objeto Response, contendo a resposta do servidor.
    """
    while True:
        response: Response = client.get(f'{ROUTE_PREFIX}/time_series/', query_string=kwargs)

        if response.status_code == TOO_MANY_REQUESTS:
            sleep(60)
        else:
            break

    return response


def response_is_in_range(response: Response, interval: timedelta) -> bool:
    """
    Verifica se a resposta recebida está no intervalo correto passado como parâmetro.
    :param interval: Intervalo de tempo entre o primeiro e o último registro
    :param response: Resposta da API.
    :return: True caso a resposta esteja no intervalo correto. False, caso contrário.
    """
    last_refreshed: datetime = datetime.fromtimestamp(response.json.get('last_refreshed') / 1000)
    first_item: datetime = datetime.fromtimestamp(response.json.get('items')[-1]['timestamp'] / 1000)

    return (last_refreshed - first_item) <= interval
