import threading
from django.db import transaction
from django.http import HttpResponse
from .models import Employee

def create_employee(request):
    print("Caller thread:", threading.get_ident())
    with transaction.atomic():
        Employee.objects.create(name="Naveen")
    return HttpResponse("Done")
