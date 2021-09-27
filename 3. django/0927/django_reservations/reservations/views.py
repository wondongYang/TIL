from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation
from django.views.decorators.http import require_http_methods, require_safe
from django.contrib.auth.decorators import login_required



def index(request):
    reservaions = Reservation.objects.all()
    context = {
        'reservations': reservaions
    }
    return render(request, 'reservations/index.html', context)

# Q3-3
# decorator를 활용하여 로그인되어 있는 사용자만 요청을 보낼 수 있고
# 로그인을 하지 않았다면, 로그인 경로로 리다이렉트
@login_required 
@require_http_methods(['GET', 'POST'])
def create(request):
    # Q3-2
    if request.method == 'POST':
        form = ReservationForm(data=request.POST) # ReservationForm 활용
        if form.is_valid(): # 데이터의 유효성 검사
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk) # 글이 저장된 후 글 상세경로로 리다이렉트
    else:
        form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'reservations/create.html', context) # 유효하지 않는 경우 입력 화면으로


@require_safe
def detail(request, pk):
    # Q4-1
    reservation = get_object_or_404(Reservation, pk=pk) # 존재하지 않는 게시글을 조회하는 경우 404 페이지를 반환
    context = {
        'reservation': reservation,
    }
    return render(request, 'reservations/detail.html', context)