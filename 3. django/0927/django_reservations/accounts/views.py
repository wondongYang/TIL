from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST

@require_http_methods(['GET', 'POST']) # GET과 POST방식을 이용하여 요청을 받음
def signup(request):
    # Q1-1
    if request.user.is_authenticated:
        return redirect('reservations:index') # 이미 로그인 된 유저는 reservations으로 리다이렉트

    if request.method == 'POST':
        form = UserCreationForm(request.POST) # UserCreationForm 활용
        if form.is_valid(): # 데이터의 유효성 검사 
            form.save()
            return redirect('accounts:login') # 회원가입 후 로그인 페이지로 리다이렉트
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context) # 유효하지 않는 경우 입력 화면으로

@require_http_methods(['GET', 'POST']) # GET과 POST방식을 이용하여 요청을 받음
def login(request):
    # Q2-1
    if request.user.is_authenticated:
        return redirect('reservations:index') # 이미 로그인 된 유저는 reservations으로 리다이렉트

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # AuthenticationForm 활용
        if form.is_valid(): # 데이터의 유효성 검사
            auth_login(request, form.get_user())
            return redirect('reservations:index') # 로그인이 정상적으로 완료되면 reservations 경로로 리다이렉트
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context) # 유효하지 않는 경우 입력 화면으로

@require_POST # decorator를 활용하여 POST메서드 요청만 승인
def logout(request):
    # Q2-2
    auth_logout(request)
    return redirect('accounts:login') # 로그아웃 이후 login 경로로 리다이렉트
