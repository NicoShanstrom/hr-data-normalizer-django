from rest_framework import serializers
from .models import Employee, Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Enrollment
    fields = [
      "plan_type",
      "carrier",
      "coverage_level",
      "effective_date",
      "term_date",
    ]

class EmployeeSerializer(serializers.ModelSerializer):
  enrollments = EnrollmentSerializer(many=True, read_only=True)

  class Meta:
    model = Employee
    fields = [
      "employee_id",
      "first_name",
      "last_name",
      "department",
      "status",
      "hire_date",
      "term_date",
      "enrollments",
    ]