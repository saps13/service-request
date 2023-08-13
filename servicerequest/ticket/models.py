from random import randint
from django.db import models

from ticket.utils import ServiceType, TicketStage

# Create your models here.

class Ticket(models.Model):
    details = models.TextField(null=True,blank=True)
    service_type = models.CharField(max_length=15, choices=ServiceType.choices,null=True, blank=True, validators=[ServiceType.validator])
    no = models.CharField(max_length=20, db_index=True, unique=True)
    stage = models.CharField(max_length=15, choices=TicketStage.choices,null=True, blank=True, validators=[TicketStage.validator])
    requestor_name = models.CharField(max_length=25,blank=True)
    requestor_address = models.CharField(max_length=50,blank=True)
    file = models.FileField(null=True,blank=True)


    def set_no(self):
        self.no = "T" + str(randint(10000000, 99999999))
        if Ticket.objects.filter(no=self.no).exists():
            self.no = "T" + str(randint(10000000, 99999999))

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.no:
            self.set_no()
        self.stage = TicketStage.Created
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
        return self
