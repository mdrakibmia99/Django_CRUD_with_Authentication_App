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