my_dict = {'key' : 'value'}

# try..
# EAFP
# 허락보다 용서를 구하는 것이 쉽다.
# 예외처리를 활용하여 검사를 수행하지 않고 일단 실행하고 예외처리를 진행하는 스타일
# 파이썬 코드가 문제 없이 '실행될 것'을 전제로 한다.
try : 
    x = my_dict['key']
except KeyError:
    pass

# if..
# LBYL
# 도약하기 전에 봐라
# 어떤 것이 실행하기전에 에러가 날만한 요소들을 조건문으로 검사를 하고 수행
if  'key' in my_dict:
    x = my_dict['key']
else:
    pass