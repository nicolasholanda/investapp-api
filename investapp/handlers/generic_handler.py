from flask import jsonify
from werkzeug.exceptions import HTTPException


def handle_generic_exception(exception: Exception):
    """
    Método responsável por tratar qualquer exceção que ocorra e devolver representada em um objeto JSON.
    :param exception: Exceção capturada pelo handler
    :return:
    """

    code = exception.code if isinstance(exception, HTTPException) else 400
    return jsonify({
        'code': code,
        'name': type(exception).__name__,
        'description': str(exception)
    }), code
