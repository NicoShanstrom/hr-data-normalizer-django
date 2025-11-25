from django.db import models

class Employee(models.Model):
  STATUS_CHOICES = [
    ("active", "Active"),
    ("terminated", "Terminated"),
    ("leave", "Leave"),
    ("unknown", "Unknown"),
  ]

  employee_id = models.CharField(max_length=32, unique=True)
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64)
  department = models.CharField(max_length=128, blank=True)
  status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="unknown")
  hire_date = models.DateField(null=True, blank=True)
  term_date = models.DateField(null=True, blank=True)

  def __str__(self):
    return f"{self.employee_id} - {self.first_name} {self.last_name}"
  
class Enrollment(models.Model):
  employee = models.ForeignKey(
    Employee,
    on_delete=models.CASCADE,
    related_name="enrollments",
  )
  plan_type = models.CharField(max_length=32) # e.g. "medical"
  carrier = models.CharField(max_length=128)  # e.g. "BlueCross"
  coverage_level = models.CharField(max_length=32)  # e.g. "employee+family"
  effective_date = models.DateField(null=True, blank=True)
  term_date = models.DateField(null=True, blank=True)

  def __str__(self):
    return f"{self.employee.employee_id} - {self.plan_type} ({self.carrier})"
