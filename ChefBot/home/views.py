from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
 
# Create your views here.
def keyboard(request):
    return JsonResponse(
        {
            'type' : 'buttons',
            'buttons' : ['1','2']
        }
    )

