from django.db import connection
from django.db.utils import OperationalError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class HealthCheckView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1;")
                cursor.fetchone()
            db_status = "ok"
            overall_status = status.HTTP_200_OK
        except OperationalError:
            db_status = "unavailable"
            overall_status = status.HTTP_503_SERVICE_UNAVAILABLE

        return Response(
            {
                "status": "ok" if db_status == "ok" else "error",
                "database": db_status,
            },
            status=overall_status,
        )
