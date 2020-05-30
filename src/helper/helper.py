from django.http import HttpResponse, JsonResponse
from django.conf import settings

def response(code, data=None, message=None, status=False, meta=None, error=None):
    if code in [200, 201]:
        status = True
        if meta==None:
            meta = {
                "page": 0,
                "limit": 0,
                "total_page": 0,
                "total_record": 0
            }

    data = data if data else []
    error = error if error else None
    message = message if message else settings.HTTP_CODE[code]

    result = {
        'code': code,
        'success' : status,
        'message': message,
        'data': data,
        'meta': meta,
        'error': error
    }
    return JsonResponse(result, status=code)