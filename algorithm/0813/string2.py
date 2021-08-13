import sys

s = ''
s1 = '가'
s2 = '가나'
s3 = '가1'

print(len(s2))
print(sys.getsizeof(s))
print(sys.getsizeof(s1))
print(sys.getsizeof(s2))
print(sys.getsizeof(s3))

print(sys.getsizeof(0))
print(sys.getsizeof(1))