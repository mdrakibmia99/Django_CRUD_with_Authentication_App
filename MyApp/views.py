from django.shortcuts import redirect, render

# Create your views here.
# Create your views here.
def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'base.html', param)
    else:
        return redirect('login')
    return render(request, 'login.html')

# sign up view 
def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        # print(uname, pwd)
        if User.objects.filter(username=uname).count()>0:
            return HttpResponse('Username already exists.')
        else:
            user = User(username=uname, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')
    
# login view 
def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('home')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'login.html')
# log out view 
def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')