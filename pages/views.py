from unittest import result
from django.shortcuts import render
from . import models
from django.db.models import Q

# Create your views here.
def HomePagesView(request):
    happy_clients = models.HappyClients.objects.all().order_by('-client_date')
    agents = models.Agents.objects.all().order_by('-date')
    blogs = models.ResentBlog.objects.all().order_by('-date')
    if request.method == 'POST':
        search_word = request.POST.get('search_word')
        search_word = str(search_word).strip()
        result = Q(name__contains = search_word) | \
                 Q(location__contains = search_word) | \
                 Q(old_prize__contains = search_word) | \
                 Q(new_prize__contains = search_word) | \
                 Q(bath_room__contains = search_word) | \
                 Q(room__contains = search_word) | \
                 Q(area__contains = search_word)

        offer_works = models.OfferWorks.objects.filter(result) 

    else:
        offer_works = models.OfferWorks.objects.all().order_by('-date')

    context = {'offer_works':offer_works,
              'happy_clients': happy_clients,
              'agents': agents,
              'blogs': blogs,
              }
    return render(request, 'index.html', context)

def AgentPagesView(request):
    if request.method == 'POST':
        search_word = request.POST.get('search_word')
        search_word = str(search_word).strip()
        result = Q(agent_name__contains = search_word)
        agents = models.Agents.objects.filter(result)
    
    else:
        agents = models.Agents.objects.all().order_by('-date')

    return render(request, 'agent.html', {'agents': agents})

def PropertiesPagesView(request):
    if request.method == 'POST':
        search_word = request.POST.get('search_word')
        search_word = str(search_word).strip()
        result = Q(name__contains = search_word) | \
                 Q(location__contains = search_word) | \
                 Q(old_prize__contains = search_word) | \
                 Q(new_prize__contains = search_word) | \
                 Q(bath_room__contains = search_word) | \
                 Q(room__contains = search_word) | \
                 Q(area__contains = search_word)
                 
        offer_works = models.OfferWorks.objects.filter(result) 

    else:
        offer_works = models.OfferWorks.objects.all().order_by('-date')
        
    return render(request, 'properties.html', {'offer_works': offer_works})

def ContactPagesView(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        models.Contact(name=name, email=email, subject=subject, message=message).save()

    return render(request, 'contact.html')

def PropertiesSinglePagesView(request, pk):
    choose_work = models.OfferWorks.objects.get(pk=pk)
    context = {'choose_work': choose_work}
    return render(request, 'properties-single.html', context)