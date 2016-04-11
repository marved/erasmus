# -*- coding: utf-8 -*-

from rest_framework.response import Response


HTTP_GENERIC_200_OK = Response(status=200)
HTTP_GENERIC_201_CREATED = Response(status=201)
HTTP_GENERIC_400_BAD_REQUEST = Response(status=400)
HTTP_GENERIC_401_NOT_AUTHORIZED = Response(status=401)
HTTP_GENERIC_403_FORBIDDEN = Response(status=403)

FORM_NOT_VALID_ERROR_MSG = u"El campo no es válido"
QUERY_NOT_VALID_ERROR_MSG = u"El campo no es válido"
INVALID_CREDENTIALS_ERROR_MSG = u"Credenciales inválidos"
USER_NOT_AUTHENTICATED_ERROR_MSG = u"El usuario no está autenticado"
THIS_FIELD_IS_REQUIRED_ERROR_MSG = "Este es un campo requerido."


def http_200_ok(message=None):
    if message:
        data = message
        return Response(status=200, data=data)
    return HTTP_GENERIC_200_OK


def http_201_created(message=None):
    if message:
        data = message
        return Response(status=201, data=data)
    return HTTP_GENERIC_201_CREATED


def http_400_bad_request(message=None):
    if message:
        data = message
        return Response(status=400, data=data)
    return HTTP_GENERIC_400_BAD_REQUEST


def http_401_not_authorized(message=None):
    if message:
        data = message
        return Response(status=401, data=data)
    return HTTP_GENERIC_401_NOT_AUTHORIZED


def http_403_forbidden(message=None):
    if message:
        data = message
        return Response(status=403, data=data)
    return HTTP_GENERIC_403_FORBIDDEN