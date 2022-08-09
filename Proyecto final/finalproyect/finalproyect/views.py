from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def primer_template(request):
    today = datetime.now()

    context={
        "name":"mario",
        "last_name":"JOSELUIS",
        "today":today    
    }

    return render(request, 'primer_template.html', context=context)
