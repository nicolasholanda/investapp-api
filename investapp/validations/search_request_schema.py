from marshmallow import Schema, fields, validate


class SearchRequestSchema(Schema):
    """
    Classe responsável por validar os parâmetros passados na query da requisição de buscar empresas.
    """

    keywords = fields.Str(required=True)
