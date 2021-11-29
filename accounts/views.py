import traceback

from django.contrib import redirects, messages
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserCreateForm, LoginForm
from accounts.models import User


login_page = "accounts/login.html"

def find_user(request):

    try:
        return User.objects.get(username=request.POST['username'], deleted_status=False)
    except Exception as e:
        return None


def login_view(request):

        if request.method=="POST":

            try:

                form = LoginForm(request.POST)
                if form.is_valid():
                    user = find_user(request)
                    if user is not None:
                        if User.check_password(user, request.POST['password']):
                            login(request, user)
                            return redirect("contacts:contacts")
                        else:
                            messages.error(request,
                                           "invalid credentials")
                            return render(request, login_page)
                    else:
                        messages.error(request,
                                       "invalid credentials")
                        return render(request, login_page)

                else:
                    messages.error(request,
                                    "invalid credentials")
                    return render(request, login_page)

            except Exception as e:
                messages.error(request,
                                "invalid credentials")
                print(traceback.format_exc())
                return render(request, login_page)
        else:
            return render(request,login_page)






def signup_view(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if form.is_valid():
            print("yest")
            user = form.save()
            # login(request, user)\
            messages.success(request,"You ve finished registering successfully, you can login now")
            return redirect('accounts:login')
        else:
            print("yest")
            messages.error(request,"Invalid form, try again ")
            return render(request, 'accounts/signup.html', {'form': form})

    else:
        form = UserCreateForm()
    return render(request, 'accounts/signup.html', {'form':form})




def logout_view(request):
    if request.GET:
        logout(request)
    return redirect('accounts:login')
