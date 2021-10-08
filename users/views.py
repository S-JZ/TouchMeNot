from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Post

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your account has been created! You are now able to log in.')
            return redirect('sign-in')
    else:
        form = UserRegisterForm()
    return render(request, 'users/sign-up.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user == post.user_name:
        Post.objects.get(pk=pk).delete()
    return redirect('profile')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
        else:
            return redirect('profile')
    else:
        user = request.user
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        user_posts = Post.objects.filter(user_name=user)
    return render(request, 'users/profile.html', {'p_form': profile_form, 'u_form': user_form, 'post_count': user_posts.count, 'posts': user_posts})


@login_required
def create_post(request):
    user = request.user
    if request.method == "POST":
        description = request.POST.get('description')
        image = request.POST.get('image')
        image = '/doodle/' + image
        user.post_set.create(description=description, pic=image)
        messages.success(request, 'Image saved successfully!')
        return redirect('profile')
    return render(request, 'users/profile.html')
