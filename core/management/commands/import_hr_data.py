import csv
from datetime import datetime
from typing import Optional

from django.core.management.base import BaseCommand
from core.models import Employee, Enrollment  

def parse_date(value: str) -> Optional[datetime.date]:
  if not value or value.strip() == "":
    return None
  
  value = value.strip()
  formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%b-%Y"]

  for fmt in formats:
    try:
      return datetime.strptime(value, fmt).date()
    except ValueError:
      continue

  return None

def normalize_status(raw_status: str) -> str:
  value = (raw_status or "").strip().lower()
  if value in {"active", "act", "a"}:
    return "active"
  if value in {"terminated", "term", "t"}:
    return "terminated"
  if value in {"leave", "loa"}:
    return "leave"
  return "unknown"

class Command(BaseCommand):
  help = "Import employeed and enrollments from CSV files"

  def add_arguments(self, parser):
    parser.add_argument("--employees", default="employees.csv")
    parser.add_argument("--enrollments", default="enrollments.csv")

  def handle(self, *args, **options):
    employees_path = options["employees"]
    enrollments_path = options["enrollments"]

    self.stdout.write(f"Importing employees from {employees_path}...")
    self.import_employees(employees_path)
    
    self.stdout.write(f"Importing enrollments from {enrollments_path}...")
    self.import_enrollments(enrollments_path)

    self.stdout.write(self.style.SUCCESS("Import complete"))

  def import_employees(self, path: str):
    with open(path, newline="") as f:
      reader = csv.DictReader(f)
      for row in reader:
        emp, created = Employee.objects.update_or_create(
          employee_id=row["employee_id"].strip(),
          defaults={
            "first_name": row["first_name"].strip(),
            "last_name": row["last_name"].strip(),
            "department": row.get("department", "").strip(),
            "status": normalize_status(row.get("status", "")),
            "hire_date": parse_date(row.get("hire_date", "")),
            "term_date": parse_date(row.get("term_date", "")),
          },
        )
        action = "Created" if created else "Updated"
        self.stdout.write(f"  {action} {emp}")

  def import_enrollments(self, path: str):
    with open(path, newline="") as f:
      reader = csv.DictReader(f)
      for row in reader:
        employee_id = row["employee_id"].strip()
        try:
          emp = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
          self.stdout.write(
            self.style.WARNING(
              f"  Skipping enrollment for unknown employee_id={employee_id}"
            )
          )
          continue

        enr = Enrollment.objects.create(
          employee=emp,
          plan_type=row["plan_type"].strip().lower(),
          carrier=row["carrier"].strip(),
          coverage_level=row["coverage_level"].strip().lower(),
          effective_date=parse_date(row.get("effective_date", "")),
          term_date=parse_date(row.get("term_date", "")),
        )
        self.stdout.write(f"  Created enrollment: {enr}")