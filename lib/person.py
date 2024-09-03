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
    def __init__(self, name="peter".capitalize(), job="Admin" ):
        self.name = name
        self.job = job
    
    #getter method for name
    def get_name(self):
        return self._name
    
    #setter method for name
    def set_name(self, name):
        if isinstance(name, str) and (len(name) >= 1 and len(name) <=25):
            self._name = name.title()
        else: 
            print("Name must be string between 1 and 25 characters.")

    # creating a property for the name
    name = property(get_name, set_name)

    #getter method for job
    def get_job(self):
        return self._job
    
    #setter method for job
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    #creating a property for job
    job = property(get_job, set_job)
    
    pass

peter = Person("peter", "carpenter")
