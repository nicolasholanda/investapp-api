from flask import Flask

from .generic_handler import handle_generic_exception


def init_app(app: Flask):
    """
    Método responsável por inicializar o módulo handlers, registrando no app um handler genérico para todas as
    exceções
    :param app: Aplicação Flask principal
    :return:
    """

    app.register_error_handler(Exception, handle_generic_exception)
