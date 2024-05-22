#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unnamed", job="Unemployed"):
        name_error = False
        job_error = False

        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            name_error = True
        else:
            self.name = name.title()

        if job not in APPROVED_JOBS and job != "Unemployed":
            print("Job must be in list of approved jobs.")
            job_error = True
        else:
            self.job = job

        if name_error:
            self.name = None
        if job_error:
            self.job = None