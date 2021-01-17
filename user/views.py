from django.shortcuts import render

# Create your views here.

from user.models import User
from django.contrib.auth.hashers import make_password,check_password

def login(req):
    return render(req,'login.html',
                  {'user':User.dummy_user(),
                   'msg': '',
                   'error': ''})

def register(req):
    return render(req,'register.html',
                  {'user':User.dummy_user(),
                   'msg': '',
                   'error': ''})

def invalid_username(username):
    #print("username",type(username))
    for x in username:
        #print("x",x)
        if x.isalpha() or x.isspace():
            pass
        else:
            return True


def invalid_email(email):
    mail = email.split('@')
    if not mail[1]=='gmail.com':
        return True

def duplicate_email(email):
    return User.objects.filter(email=email)

def register_save(req):
    if req.method=='POST':
        formdata = req.POST

        username = formdata['username']
        email = formdata['email']
        password = formdata['password']

        userobj = User(userName=username, email=email, password=password)

        if username=="" or email=="" or password=="":
            return render(req, 'register.html',
                          {'user':{'userName':username, 'email':email},
                           'msg':'',
                           'error':'Invalid Credentials...'})

        invalidUserName = invalid_username(username)
        if invalidUserName:
            return render(req, 'register.html',
                          {'user':{'userName':username, 'email':email},
                           'msg':'',
                           'error':'Invalid User Name...'})

        invalidEmail = invalid_email(email)
        if invalidEmail:
            return render(req, 'register.html',
                          {'user': {'userName':username, 'email':email},
                           'msg': '',
                           'error': 'Invalid Email Id...'})

        duplicateEmail = duplicate_email(email)
        if duplicateEmail:
            return render(req, 'login.html',
                          {'user': {'email':email},
                           'msg': '',
                           'error': 'User Already Exists...'})

        hash_pass = make_password(password)  # make_password is create encrypt password
        #print('-----------pass hash:', hash_pass)
        addUser = User(userName=username, email=email, password=hash_pass)
        addUser.save()

        return render(req, 'login.html',
                      {'user': addUser,
                       'msg': 'User Registration Successfully...',
                       'error': ''})
    else:
        return render(req, 'register.html',
                      {'user': User.dummy_user(),
                       'msg': '',
                       'error': ''})

def login_success(req):
    if req.method=='POST':
        formdata = req.POST

        email = formdata['email']
        password = formdata['password']
        if email=="" or password=="":
            return render(req, 'login.html',
                          {'user':{'email':email},
                           'msg':'',
                           'error':'Invalid Credentials...'})

        invalidEmail = invalid_email(email)
        if invalidEmail:
            return render(req, 'login.html',
                          {'user': {'email':email},
                           'msg': '',
                           'error': 'Invalid Email Id...'})

        user = User.objects.filter(email=email).first()
        if user:
            # check password decrypted format  #password hashing
            check_pass = check_password(password,user.password)
            if check_pass:
                req.session['email'] = user.email
                return render(req, 'home.html',
                              {'user': {'email': email},
                               'msg': 'Welcome To Trello...',
                               'error': ''})
            else:
                return render(req, 'login.html',
                              {'user': {'email':email},
                               'msg': '',
                               'error': 'Invalid Password...'})
        else:
            return render(req, 'register.html',
                          {'user': User.dummy_user(),
                           'msg': '',
                           'error': 'Invalid User...Register First...'})


    else:
        return render(req, 'login.html',
                      {'user': User.dummy_user(),
                       'msg': 'User Registration Successfully...',
                       'error': ''})

def home_page(req):
    if not req.session.has_key('email'):
        return user_loginout(req)

    user = User.objects.filter(email = req.session['email']).first()
    return render(req, 'home.html',
                  {'user': user,
                   'msg': '',
                   'error': ''})

def user_loginout(req):
    if req.session.has_key('email'):
        del req.session['email']
        return render(req, 'login.html',
                      {'user': User.dummy_user(),
                       'msg': 'Logout...',
                       'error': ''})
    else:
        return render(req, 'login.html',
                      {'user': User.dummy_user(),
                       'msg': 'Login First...',
                       'error': ''})
