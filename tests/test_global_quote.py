from http.client import OK, TOO_MANY_REQUESTS, BAD_REQUEST, NOT_FOUND
from time import sleep

from flask import Response
from flask.testing import FlaskClient

from investapp.utils.constants import AV_GLOBAL_QUOTE_KEYS


ROUTE_PREFIX = '/stock_exchange'


def test_should_return_company_global_quote(client: FlaskClient):
    """
    Testa se a API retorna a cotação global por empresa.
    :param client: API cliente para testes.
    :return:
    """
    company_symbol = 'XIACF'
    response: Response = get_global_quote_by_symbol(client, symbol=company_symbol)

    assert response.status_code == OK
    assert response.json.get('symbol') == company_symbol
    for key in AV_GLOBAL_QUOTE_KEYS.keys():
        assert response.json.get(key) is not None


def test_should_fail_when_symbol_is_missing(client: FlaskClient):
    """
    Testa se a API retorna um erro quando o símbolo não é enviado.
    :param client: API cliente para testes.
    :return:
    """
    response: Response = get_global_quote_by_symbol(client)

    assert response.status_code == NOT_FOUND


def test_should_fail_when_symbol_is_invalid(client: FlaskClient):
    """
    Testa se a API retorna um erro quando o símbolo enviado não é reconhecido pelo Alpha Vantage
    :param client: API cliente para testes.
    :return:
    """
    response: Response = get_global_quote_by_symbol(client, symbol='9X9X9X9X')

    assert response.status_code == BAD_REQUEST
    assert 'global vazia' in response.json.get('description')


def test_should_fail_when_many_requests_are_made(client: FlaskClient):
    """
    Testa se a API retorna um erro quando mais do ques 5 requisições são feitas dentro de 1 minuto.
    :param client: API cliente para testes.
    :return:
    """
    while True:
        response = client.get(f'{ROUTE_PREFIX}/global_quote/XIACF')
        if response.status_code != OK:
            break

    assert response.json.get('code') == TOO_MANY_REQUESTS
    assert 'Muitas requisições' in response.json.get('description')


def get_global_quote_by_symbol(client: FlaskClient, **kwargs) -> Response:
    """
    Retorna a cotação global de pontos por empresa e garante que o servidor não retorne uma exceção
    do tipo TooManyRequests.
    :param client: API cliente para testes.
    :key symbol: Símbolo da empresa desejada.
    :return: Objeto Response, contendo a resposta do servidor.
    """
    symbol = kwargs.get('symbol') if kwargs.get('symbol') is not None else ''
    while True:
        response: Response = client.get(f'{ROUTE_PREFIX}/global_quote/{symbol}')

        if response.status_code == TOO_MANY_REQUESTS:
            sleep(60)
        else:
            break

    return response
