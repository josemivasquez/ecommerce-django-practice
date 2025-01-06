from django.shortcuts import render, redirect
from ..models import Person
from ..forms import PersonLoginForm, PersonLogupForm


def user_logout(request):
    request.session["actual_user"] = None
    return redirect("/")

def user_login(request):
    if request.method == 'POST':
        return post_user_login(request)
    
    return render(request, 'user_login.html', {
        'form' : PersonLoginForm
    })
    
def post_user_login(request):
    dni = request.POST.get('dni')
    login_password = request.POST.get('password')

    user = Person.objects.get(dni=dni)
    true_password = user.password
    
    if login_password == true_password:
        request.session['actual_user'] = dni
        request.session.modified = True
        return redirect('/main')
    
    else:
        return redirect('/user_login')
   
def user_logup(request):
    if request.method == 'POST':
        return post_user_logup(request)

    return render(request, 'user_logup.html', {
        'form' : PersonLogupForm
    })

def post_user_logup(request):
    dni = request.POST.get('dni')
    name = request.POST.get('name')
    password = request.POST.get('password')
    email = request.POST.get('email')
    
    user = Person(dni=dni, name=name, password=password, email=email)
    user.save()
    
    request.session['actual_user'] = dni
    request.session.modified = True
    return redirect('/main')