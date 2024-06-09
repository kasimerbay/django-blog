from django.shortcuts import render
from django.http import Http404
from datetime import datetime
from .models import *


# Create your views here.

content = {
        "navs": list(Navs.objects.all()),
        "name":"A. Kasım Erbay",
        "date":datetime.now().date,
    }



def papers(request):
        papers = Paper.objects.all()
        infos = Contact.objects.all()
        # return render(request, "blog/papers.html", {"content":content,"posts":papers, "infos":infos})
        try:
            papers = Paper.objects.all()
            return render(request, "blog/papers.html", {"content":content,"posts":papers})
        except:
            raise Http404()


def contact(request):
    infos = Contact.objects.all()

    try:
        return render(request, "blog/contact.html", {"content":content, "infos":infos})
    except:
        raise Http404()


