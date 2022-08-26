from django.shortcuts import render
from .models import Registration

# Create your views here.


def index(request):
    if request.method == "POST":
        data = None
        error = None
        context = {}

        registration_number = request.POST.get("registration_number")

        try:
            data = Registration.objects.get(registration_number=registration_number)
            context = {"data": data}
        except Registration.DoesNotExist:
            error = "Vehicle does not exist"

        if error:
            context = {**context, "error": error}
        return render(request, "vehicle/index.html", context)

    return render(request, "vehicle/index.html")
