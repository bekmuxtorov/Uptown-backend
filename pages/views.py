from django.shortcuts import render
from . import models

# Create your views here.
def HomePagesView(request):
    offer_works = models.OfferWorks.objects.all().order_by('-date')
    happy_clients = models.HappyClients.objects.all().order_by('-client_date')
    agents = models.Agents.objects.all().order_by('-date')
    blogs = models.ResentBlog.objects.all().order_by('-date')

    context = {'offer_works':offer_works,
              'happy_clients': happy_clients,
              'agents': agents,
              'blogs': blogs,
              }
    return render(request, 'index.html', context)

def AgentPagesView(request):
    agents = models.Agents.objects.all().order_by('-date')
    return render(request, 'agent.html', {'agents': agents})

def PropertiesPagesView(request):
    offer_works = models.OfferWorks.objects.all().order_by('-date')
    return render(request, 'properties.html', {'offer_works': offer_works})

def ContactPagesView(request):
    return render(request, 'contact.html')

def PropertiesSinglePagesView(request, pk):
    choose_work = models.OfferWorks.objects.get(pk=pk)
    context = {'choose_work': choose_work}
    return render(request, 'properties-single.html', context)