from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
