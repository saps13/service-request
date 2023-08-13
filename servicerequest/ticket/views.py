

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ticket.forms import StatusForm, TicketForm
from ticket.models import Ticket
from ticket.utils import TICKET_STATUS

@csrf_exempt
def service(request):
    # print("received")
    form = TicketForm()
    context = {"form": form}
    if request.method == "POST":
        # print("post",request.POST)
        form = TicketForm(request.POST,request.FILES)
        # for field in form:
        #     print("Field Error:", field.name,  field.errors)

        if form.is_valid():
            # print("here")
            tkt = form.save(commit=True)
            tkt = tkt.save()
            # print("number",tkt.no)
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
            print(ticket)
            if ticket:
                context.update({'post_output': TICKET_STATUS[ticket.stage]})
                print("ctx",context)

            else:
                context.update({'post_output': "Not found"})

    return render(request, "status.html", context)
