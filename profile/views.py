# profile/views.py

from django.shortcuts import render

def profile_index(request):
    """
    Renders the main “resume” page for this app.
    We expect an index.html under templates/profile/index.html.
    """
    return render(request, 'profile/index.html')

def resume(request):
    """View function for the resume page."""
    return render(request, 'resume.html')
