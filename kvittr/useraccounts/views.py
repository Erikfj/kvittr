from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from useraccounts.models import User

# Create your views here.
def user_listing(request):
    useraccounts = User.objects.all()
    context = {'useraccounts': useraccounts}
    return render(request, 'useraccounts/user_listing.html', context)

def user_details(request, useraccounts_id):
    useraccounts = User.objects.get(pk=useraccounts_id)
    context = {'useraccounts': useraccounts}
    return render(request, 'useraccounts/student_details.html', context)

@csrf_exempt
def user_increase_like(request, useraccounts_id):
	accounts = User.objects.get(pk=useraccounts_id)
	useraccounts.passed_exams = useraccounts.passed_exams + 1
	useraccounts.save()
	data = {'like_updated': useraccounts.passed_exams}
	return JsonResponse(data)
