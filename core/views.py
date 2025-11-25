from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
  """
  Read-only API for employees + their enrollments. This is basically a DRF version of serializers from Rails land
  """
  queryset = Employee.objects.all().order_by("employee_id")
  serializer_class = EmployeeSerializer
