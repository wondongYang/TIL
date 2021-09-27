from django.contrib import admin
from .models import Reservation

# Q3-1
# 관리자 페이지에서 조회, 생성, 수정, 삭제가 가능하도록 구현
admin.site.register(Reservation)