from django.db import models


class Lease(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    # Relationships:
    # complex = models.ForeignKey('real_estate.Complex')
    unit = models.OneToOneField('real_estate.Unit')

    def __str__(self):
        return self.unit.address + ' ' + self.unit.city + ' ' + self.unit.state + ' #' + self.unit.unit_number
    
    # def save(self, *args, **kwargs):
    #     print('Length: ', self.length)
    #     print('End date: ', self.start_date + self.length)
    #     self.end_date = self.start_date + self.length
    #     super(Lease, self).save(*args, **kwargs)