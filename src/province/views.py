from django.core.paginator import Paginator, EmptyPage
from django.db import transaction
from django.conf import settings
from rest_framework.views import APIView

from src.helper.helper import response

from src.province.serializer import ProvinceSerializer
from src.province.models import Province

class ProvinceView(APIView):
    def get(self, request, id=None):
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)

        try:
            if id:
                serializer = ProvinceSerializer(Province.objects.get(id=id))
                if serializer.data:
                    return response(code=200, data=serializer.data)

            data = Province.objects.all().order_by("name")
            pagination = Paginator(data, limit)
            serializer = ProvinceSerializer(pagination.page(page), many=True)
        except (EmptyPage, Province.DoesNotExist):
            return response(code=200, data=[], message="data not found")

        if serializer.data:
            meta = {
                "page": int(page),
                "limit": int(limit),
                "total_page": pagination.num_pages,
                "total_record": pagination.count
            }
            return response(code=200, data=serializer.data, meta=meta)

    def post(self, request):
        request_body = request.data
        try:
            serializer = ProvinceSerializer(data=request_body)
            if serializer.is_valid():
                serializer.save()
                return response(code=201, message="")
        except Exception:
            return response(code=400, message="error")

    def put(self, request, id):
        request_body = request.data
        try:
            data = Province.objects.get(id=id)
            serializer = ProvinceSerializer(data, data=request_body)
            if serializer.is_valid():
                serializer.save()
                return response(code=202, message="")
        except Province.DoesNotExist:
            return response(code=400, message=settings.MESSAGE_NOT_EXIST.format("province"))
        except Exception as e:
            return response(code=400, error=e)

    def delete(self, request, id):
        try:
            data = Province.objects.get(id=id)
            if data:
                data.delete()
                return response(code=202, message="")
        except Province.DoesNotExist:
            return response(code=400, message=settings.MESSAGE_NOT_EXIST.format("province"))
        except Exception as e:
            return response(code=400, error=e)