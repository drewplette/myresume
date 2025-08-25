from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count
from collections import defaultdict
from profile.models import Blog, Comment

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
    posts = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})

def scripts(request):
    """View function for the scripts page."""
    return render(request, 'scripts.html')

def contact(request):
    """View function for the contact page."""
    return render(request, 'contact.html')

def blog_detail(request, post_id):
    """View function for individual blog post."""
    post = get_object_or_404(Blog, id=post_id)
    comments = post.comments.all().order_by('-created_at')
    
    if request.method == 'POST':
        # Handle comment submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        
        if name and email and content:
            Comment.objects.create(
                blog=post,
                name=name,
                email=email,
                content=content
            )
            messages.success(request, 'Your comment has been posted successfully!')
            return redirect('blog_detail', post_id=post.id)
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    return render(request, 'blog_detail.html', {'post': post, 'comments': comments})

def blog_archive(request):
    """View function for blog archive page."""
    selected_year = request.GET.get('year')
    
    if selected_year:
        posts = Blog.objects.filter(created_at__year=selected_year).order_by('-created_at')
    else:
        posts = Blog.objects.all().order_by('-created_at')
    
    # Organize posts by year and month
    posts_by_year = defaultdict(lambda: defaultdict(list))
    for post in posts:
        year = post.created_at.year
        month = post.created_at.strftime('%B')
        posts_by_year[year][month].append(post)
    
    # Get available years
    years = Blog.objects.dates('created_at', 'year', order='DESC')
    years = [date.year for date in years]
    
    # Calculate stats
    total_posts = Blog.objects.count()
    total_comments = Comment.objects.count()
    total_years = len(years)
    
    context = {
        'posts_by_year': dict(posts_by_year),
        'years': years,
        'selected_year': int(selected_year) if selected_year else None,
        'total_posts': total_posts,
        'total_comments': total_comments,
        'total_years': total_years,
    }
    
    return render(request, 'blog_archive.html', context)