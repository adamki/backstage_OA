from django.http import JsonResponse

from api.models import NumberRequest
from api.calculations import calculate_difference


def difference_view(request):
    query_params = request.GET.get("n")
    n = query_params.get("n")

    # Check if the only parameter is 'n' and that it's not None
    if len(query_params) != 1 or n is None:
        error_message = "Invalid parameters. Only 'n' is allowed." if len(query_params) != 1 else "No number provided"
        return JsonResponse({"error": error_message}, status=400)

    try:
        n = int(n)
        number_request, created = NumberRequest.objects.get_or_create(
            number=n, defaults={"value": calculate_difference(n)}
        )

        if not created:
            number_request.increment()

        number_request.save()
        return JsonResponse(number_request.to_json())

    except ValueError:
        return JsonResponse({"error": "Invalid number"}, status=400)
