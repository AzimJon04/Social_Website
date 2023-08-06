# from email.message import EmailMessage
# from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import UpdateView

from .forms import UserForm, UserProfileForm
from .models import UserProfile

# Create your views here.


# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             # save form in the memory not in database
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             # to get the domain of the current site
#             current_site = get_current_site(request)
#             mail_subject = 'Activation link has been sent to your email id'
#             message = render_to_string('authentication/acc_active_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': str(user.pk),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(
#                 mail_subject, message, to=[to_email]
#             )
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = SignupForm()
#     return render(request, 'authentication/signup.html', {'form': form})


# def activate(request, uid):
#     User = get_user_model()

#     try:
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None:
#         # The user is valid
#         user.is_active = True
#         user.save()
#         return redirect('signin')
#     else:
#         # The user is not valid
#         return HttpResponse('Activation link is invalid!')


def register(request):
    userform = UserForm(request.POST or None)
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('/account/login')
    return render(request, 'registration/register.html', {'userform': userform})


def profile_list(request, pk):
    profiles = UserProfile.objects.exclude(user=request.user)
    profile = UserProfile.objects.get(pk=pk)
    context = {'profile': profile, 'profiles': profiles}
    if request.method == 'POST':
        current_user_profile = request.user.userprofile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, 'account/profile_list.html', context)


def profile(request, pk):
    profile = UserProfile.objects.get(pk=pk)
    profiles = UserProfile.objects.exclude(user=request.user)
    context = {'profile': profile, 'profiles': profiles}
    return render(request, 'account/profile.html', context)


class ProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'account/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    def get_success_url(self):
        return reverse('registration:profile', kwargs={'pk': self.object.pk})
