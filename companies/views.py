from django.shortcuts import render

def company_dashboard(request):
    return render(request, "companies/dashboard.html")