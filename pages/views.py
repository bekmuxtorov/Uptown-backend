from django.shortcuts import render

# Create your views here.
def HomePagesView(request):
    return render(request, 'index.html')

def AgentPagesView(request):
    return render(request, 'agent.html')

def PropertiesPagesView(request):
    return render(request, 'properties.html')

def ContactPagesView(request):
    return render(request, 'contact.html')

def PropertiesSinglePagesView(request):
    return render(request, 'properties-single.html')