from marshmallow import Schema, fields, validate


class GlobalQuoteRequestSchema(Schema):
    """
    Classe responsável por validar os parâmetros passados na query da cotação global por
    empresa.
    """

    symbol = fields.Str(required=True, validate=validate.Length(min=1))
