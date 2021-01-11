from django.shortcuts import render,redirect
from django.contrib import messages, auth

from .forms import LoginForm, RegisterForm



def RegisterPage(request):
    form = RegisterForm(request.POST or None)
    context = {
            'form' : form
            }
    template = 'signUpPage.html'

    if form.is_valid():
        form.save()
        messages.success(request, "Pendaftaran akun sukses")
    else:
        messages.error(request, "Pendaftaran akun gagal")
    return render(request, template, context)


def LoginPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email , password=password)

        if user is not None:
            auth.login(request, user)
            print('login')
            return redirect("/")
        else:
            messages.error(request, "anda salah memasukkan akun atau akun tidak ada")
            return redirect('signin')

    return render(request, "signin.html")


def logout(request):
    auth.logout(request)
    messages.success(request, "anda berhasil keluar")
    return redirect('/')

