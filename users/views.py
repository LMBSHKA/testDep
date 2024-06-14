from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

from users.forms import ProfileForm, UploadForm, UserLoginForm, UserRegistrationForm, EditProfileForm
from users.models import Upload_images, User

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = r'users\edit_profile.html'
    success_url = reverse_lazy('users:profile')
    def get_object(self):
        return self.request.user


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                    
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html')


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            
            messages.success(request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    users_uploads = Upload_images.objects.filter(user_id=request.user.id)
    count_default = Upload_images.objects.filter(user_id=request.user.id, category="defoult").count()
    count_achive = Upload_images.objects.filter(user_id=request.user.id, category="achivements").count()
    all_count = count_default + count_achive
    context = {
        'form': form,
        'users_uploads': users_uploads,
        'count': all_count,
    }
    return render(request, 'users/profile.html', context)

def list_images(request):
    if request.method == "POST":
        Upload_images.objects.create(user_id=request.user.id,
                                     image=request.FILES.get('image'),
                                     category="defoult")
        #form = UploadForm(request.POST, request.FILES)
        #if form.is_valid():
            #form.save()
   # else:
        #context = {'form': UploadForm(request.POST, request.FILES)}
        #return render(request, 'users/list.html', context)
    users_uploads = Upload_images.objects.filter(user_id=request.user.id)
    context = {'form': UploadForm(), 'users_uploads': users_uploads}
    return render(request, 'users/list.html', context)

def list_images_achivements(request):
    if request.method == "POST":
        Upload_images.objects.create(
            user_id=request.user.id,
            image=request.FILES.get('image'),
            category='achivements')
    users_uploads = Upload_images.objects.filter(user_id=request.user.id)
    context = {'form': UploadForm(), 'users_uploads': users_uploads }
    return render(request, 'users/list_achive.html', context)
    
def equipments(request):
    return render(request, 'users/equipments.html')

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))

