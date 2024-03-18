from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def contact_form(request):
    context = {
        'success': True,
        'message_sent': 'Contact form sent successfully'
    }
    return JsonResponse(context)

def contact(request):
    return render(request, 'contact.html')
