

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ticket.forms import StatusForm, TicketForm
from ticket.models import Ticket
from ticket.utils import TICKET_STATUS

@csrf_exempt
def service(request):
    form = TicketForm()
    context = {"form": form}
    if request.method == "POST":
        form = TicketForm(request.POST,request.FILES)

        if form.is_valid():
            tkt = form.save(commit=True)
            tkt = tkt.save()
            context.update({'post_output': tkt.no})
    return render(request, "ticket.html", context)

@csrf_exempt
def status(request):
    form = StatusForm()
    context = {"form": form}
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            ticket_no = form.cleaned_data["no"]
            ticket = Ticket.objects.filter(no=ticket_no).first()
            if ticket:
                context.update({'post_output': TICKET_STATUS[ticket.stage]})

            else:
                context.update({'post_output': "Not found"})

    return render(request, "status.html", context)
