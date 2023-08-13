from django import forms
from ticket.models import Ticket

# iterable
ServiceTypeChoices =(
    ("NI","New Installations"),
    ("SEC","Service Existing Connection"),
    ("RC","Remove Connection"),
    ("ENQ","Enquiry"),
)
class TicketForm(forms.ModelForm):
    details = forms.Textarea()
    service_type = forms.ChoiceField(choices=ServiceTypeChoices)
    requestor_name = forms.CharField()
    requestor_address = forms.CharField()
    file = forms.FileField(required=False)
    class Meta:
        model = Ticket
        exclude = ("no", "stage")

class StatusForm(forms.Form):
    no = forms.CharField()