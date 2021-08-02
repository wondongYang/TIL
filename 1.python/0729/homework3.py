a = 1/0 #=> ZeroDivisionError, 어떤 수를 0으로 나눴을 시 발생

print(b) #=> NameError, 지정하지 않은 어떤 변수를 불렀을 시 발생

c = [1, 2, 3] 
d = '123'
print(c + d) #=> TypeError, 연산을 실행시 서로 다른 타입으로 인해 불가능할 시 발생

e = [1, 2]
print(e[3]) #=> IndexErrpr, 범위를 벗어나서 호출 시 발생

f = {'1': 1, '2': 2}
f['3'] #=> KeyError, 없는 키 값을 호출 시 발생

import ab #=> ModuleNotFoundError, 없는 모듈을 호출 시 발생

from abc import g #-> ImportError, 패키지에서 잘못된 이름의 모듈을 호출 시 발생
