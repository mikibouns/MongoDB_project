from django.shortcuts import render, HttpResponseRedirect, reverse
from . forms import UserLoginForm, UserRegisterForm
from django.contrib import auth


def login(request):
    current_path = request.META.get('HTTP_REFERER')
    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(current_path)

    return HttpResponseRedirect(current_path)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def registration(request):
    # current_path = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('main:main_page'))
    else:
        register_form = UserRegisterForm()
    content = {'register_form': register_form}
    return render(request, 'auth_app/register.html', content)


# def edit(request):
#     title = 'редактирование'
#     if request.method == 'POST':
#         edit_form = UserEditForm(request.POST, request.FILES,
#                                      instance=request.user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('auth:edit'))
#     else:
#         edit_form = UserEditForm(instance=request.user)
#     content = {'title': title, 'edit_form': edit_form, 'collections': wallpaper_collections}
#     return render(request, 'authapp/edit.html', content)