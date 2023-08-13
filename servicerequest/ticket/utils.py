from djchoices.choices import DjangoChoices, ChoiceItem


class ServiceType(DjangoChoices):
    NewInstallation = ChoiceItem("NI")
    ServiceOnExistingConnection = ChoiceItem("SEC")
    RemoveConnection = ChoiceItem("RC")
    Enquiry = ChoiceItem("ENQ")

class TicketStage(DjangoChoices):
    Created = ChoiceItem("Cr")
    Progress = ChoiceItem("Pr")
    Done = ChoiceItem("Dn")

TICKET_STATUS = {
    'Cr': 'Ticket Created',
    'Pr': 'Work under process',
    'Dn': 'Completed'
}