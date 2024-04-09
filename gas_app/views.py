from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm,UserRegistrationForm
from django.utils import timezone

def home(request):
    return render(request, 'home.html')

def home2(request):
    return render(request, 'home2.html')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home2')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.submitted_at = timezone.now()
            service_request.save()
            return redirect('request_submitted')  
    else:
        form = ServiceRequestForm()
    return render(request, 'service_request.html', {'form': form})

def request_submitted(request):
    return render(request, 'request_submitted.html')

@login_required
def track_request_status(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'track_request.html', {'service_requests': service_requests})

def some_view(request):
    return redirect('home2')

def generate_bill_pdf(request, request_id):
    service_request = get_object_or_404(ServiceRequest, pk=request_id)
    
    user = service_request.customer
    full_name = f"{user.first_name} {user.last_name}" if user.first_name and user.last_name else user.username
    user_details = {
        'full_name': full_name,
        'email': user.email,
        'phone': user.phone if hasattr(user, 'profile') else ''
    }
    
    # Render bill template with user details
    template_path = 'bill_template.html'
    context = {'service_request': service_request, 'user_details': user_details}
    template = get_template(template_path)
    html = template.render(context)
    
    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="bill_{request_id}.pdf"'
    
    # Generate PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Failed to generate PDF: %s' % pisa_status.err)
    
    return response 
