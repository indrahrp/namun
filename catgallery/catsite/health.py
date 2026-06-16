import json

from django.db import connection, OperationalError
from django.http import JsonResponse


def health_check(request):
    """
    Health check endpoint that tests the database connection.

    Returns 200 OK with DB status if the connection is healthy,
    or 500 with error details if the connection fails. Use this
    to diagnose whether a Supabase DATABASE_URL is reachable from
    the Railway runtime.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
    except OperationalError as e:
        return JsonResponse(
            {
                "status": "error",
                "database": "unreachable",
                "detail": str(e),
            },
            status=500,
        )
    except Exception as e:
        return JsonResponse(
            {
                "status": "error",
                "database": "unknown",
                "detail": str(e),
            },
            status=500,
        )

    return JsonResponse(
        {
            "status": "ok",
            "database": "reachable",
        },
        status=200,
    )
