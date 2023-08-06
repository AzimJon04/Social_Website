from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import PostProfile
from .forms import PostForm, CommentForm
from account.models import UserProfile
# Create your views here.



@login_required
def dashboard(request):
    form = PostForm(request.POST or None)
    user_profile = request.user.userprofile
    user_ip = get_client_ip(request)

    if not user_profile.last_login_ip or user_profile.last_login_ip != user_ip:
        user_profile.last_login_ip = user_ip
        user_profile.save()

    if request.method == 'POST':
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect('publications:dashboard')

    followed_posts = PostProfile.objects.filter(
        user__userprofile__in = request.user.userprofile.follows.all()
        ).order_by('-created_at')
    context = {
        'form': form,
        'userposts': followed_posts,
        'user_profile': user_profile,
    }
    return render(
        request,
        'publications/dashboard.html',
        context
        )


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def post_user(request, pk):
    form = CommentForm(request.POST or None)
    post = PostProfile.objects.get(pk=pk)
    current_user = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        reaction = request.POST.get('like')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_comment = request.user
            comment.save()
            post.comment.add(comment)
            return redirect('publications:post_user', pk=pk)
        if reaction == 'like':
            post.user_like.add(current_user)
            post.save()
            if current_user in post.user_dislike.all():
                post.user_dislike.remove(current_user)
                post.save()
                return redirect('publications:post_user', pk=pk)
        if reaction == 'dislike':
            post.user_dislike.add(current_user)
            post.save()
            if current_user in post.user_like.all():
                post.user_like.remove(current_user)
                post.save()
                return redirect('publications:post_user', pk=pk)
    context = {'post': post, 'form': form}
    return render(request, 'publications/post_user.html', context)
