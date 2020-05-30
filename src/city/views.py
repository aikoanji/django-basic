from django.core.paginator import Paginator, EmptyPage
from rest_framework.views import APIView

from src.helper.helper import response

from src.city.serializer import CitySerializer
from src.city.models import City

class CityView(APIView):
    def get(self, request, id=None):
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)

        try:
            if id:
                serializer = CitySerializer(City.objects.get(id=id))
                if serializer.data:
                    return response(code=200, data=serializer.data)

            data = City.objects.all().order_by("name")
            pagination = Paginator(data, limit)
            serializer = CitySerializer(pagination.page(page), many=True)
        except (EmptyPage, City.DoesNotExist):
            return response(code=200, data=[], message="data not found")

        if serializer.data:
            meta = {
                "page": int(page),
                "limit": int(limit),
                "total_page": pagination.num_pages,
                "total_record": pagination.count
            }
            return response(code=200, data=serializer.data, meta=meta)