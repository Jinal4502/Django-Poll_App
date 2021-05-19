from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


array = ['Python', 'Java', 'C', 'C++', 'C#', 'DotNet', 'HTML', 'JavaScript', 'PHP', 'Swift', 'SQL', 'CSS', 'Kotlin']
count = dict()

def index(request):
    dictionary = {
        "array": array
    }
    return render(request, 'index.html', context=dictionary)

def getquery(request):
    q = request.GET['languages']
    if q in count:
        # increement count for existing query in the dictionary
        count[q] = count[q] + 1
    else:
        # first occurence
        count[q] = 1
    dictionary = {
        "array": array,
        "count": dict(sorted(count.items(), key=lambda x:x[1], reverse=True))
    }
    return render(request, 'index.html', context=dictionary)