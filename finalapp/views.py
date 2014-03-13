from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')



# if request.user.is_employer:
#     request.user.employer.company_name
#     request.user.employer.phone_number


