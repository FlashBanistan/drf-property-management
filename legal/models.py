from django.db import models

class Term(models.Model):
    period = models.DurationField()


class Lease(models.Model):
    start_date = models.DateField()
    # Relationships:
    term = models.ForeinKey(Term, on_delete=models.PROTECT)