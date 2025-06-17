from django.shortcuts import render

def home(request):
    """View function for the home page."""
    return render(request, 'home.html')

def profile(request):
    """View function for the profile page."""
    return render(request, 'profile.html')

def resume(request):
    """View function for the resume page."""
    return render(request, 'resume.html')

def portfolio(request):
    """View function for the portfolio page."""
    return render(request, 'portfolio.html')
def blog(request):
    """View function for the blog page."""
    return render(request, 'blog.html')