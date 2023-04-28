from django.shortcuts import render, redirect
from .models import Customer
from .forms import RegisterationForm

# Create your views here.

def index(request):
    if request.method == 'POST':
         form = RegisterationForm(request.POST)
         if form.is_valid(): 
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            date_of_birth = request.POST.get('date_of_birth')
            gender = request.POST.get('gender')
            country = request.POST.get('country')
            state = request.POST.get('state')
            town = request.POST.get('town')
            zip_code = request.POST.get('zip_code')
            phone = request.POST.get('phone')
            phone2 = request.POST.get('phone2')
            email = request.POST.get('email')
            return redirect(request, 'index', 
                            first_name=first_name,
                            last_name=last_name,
                            date_of_birth=date_of_birth,
                            gender=gender,
                            country=country,
                            state=state,
                            town=town,
                            zip_code=zip_code,
                            phone=phone,
                            phone2=phone2,
                            email=email)
    else:
        form = RegisterationForm()
    return render(request, 'index.html', {'form': form})

def indexx(request):
    return render(request, 'indexx.html')