from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
  """
  Read-only API for employees + their enrollments.
  """
  queryset = Employee.objects.all().order_by("employee_id")
  serializer_class = EmployeeSerializer
  lookup_field = "employee_id"
