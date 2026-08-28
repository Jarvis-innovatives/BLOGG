from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import AboutMe, BlogPost, Certificate, Skill, Project, ContactMessage

def home_view(request):
    about_me = AboutMe.objects.first()
    skills = Skill.objects.all()
    certificates = Certificate.objects.all()
    projects = Project.objects.all()
    recent_posts = BlogPost.objects.filter(is_published=True)[:3]
    
    context = {
        'about_me': about_me,
        'skills': skills,
        'certificates': certificates,
        'projects': projects,
        'recent_posts': recent_posts,
    }
    return render(request, 'index.html', context)


def blog_list_view(request):
    tag = request.GET.get('tag', 'All')
    search_query = request.GET.get('q', '').strip()
    sort_by = request.GET.get('sort', 'latest')

    posts = BlogPost.objects.filter(is_published=True)

    if tag and tag != 'All':
        posts = posts.filter(tag__iexact=tag)

    if search_query:
        posts = posts.filter(title__icontains=search_query) | posts.filter(summary__icontains=search_query)

    if sort_by == 'oldest':
        posts = posts.order_by('created_at')
    elif sort_by == 'title':
        posts = posts.order_by('title')
    else: # latest
        posts = posts.order_by('-created_at')

    tags = ['All', 'Networking', 'Cybersecurity', 'Mobile', 'Career', 'Projects', 'Mindset']

    # Handle AJAX filtering/sorting requests for seamless client-side updates
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        data = [
            {
                'id': post.id,
                'title': post.title,
                'slug': post.slug,
                'tag': post.tag,
                'date': post.date_display,
                'read_time': post.read_time,
                'summary': post.summary,
                'img': post.get_image_url,
                'content': post.content_json,
            }
            for post in posts
        ]
        return JsonResponse({'posts': data})

    context = {
        'posts': posts,
        'tags': tags,
        'selected_tag': tag,
        'selected_sort': sort_by,
        'search_query': search_query,
    }
    return render(request, 'blog_list.html', context)


def blog_detail_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    related_posts = BlogPost.objects.filter(is_published=True).exclude(id=post.id)[:2]
    next_post = BlogPost.objects.filter(is_published=True, created_at__lt=post.created_at).order_by('-created_at').first()
    if not next_post:
        next_post = BlogPost.objects.filter(is_published=True).exclude(id=post.id).first()
    context = {
        'post': post,
        'related_posts': related_posts,
        'next_post': next_post,
    }
    return render(request, 'blog_detail.html', context)


@csrf_exempt
def contact_api(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                body = json.loads(request.body)
                name = body.get('name')
                email = body.get('email')
                message = body.get('message')
            else:
                name = request.POST.get('name')
                email = request.POST.get('email')
                message = request.POST.get('message')

            if name and email and message:
                ContactMessage.objects.create(name=name, email=email, message=message)
                return JsonResponse({'status': 'success', 'message': 'Thank you! Your message has been sent.'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Please fill in all required fields.'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)
