# 모음은 몇 개나 있을까?

def count_vowels(a):
    vowel_a = a.count('a')
    vowel_e = a.count('e')
    vowel_i = a.count('i')
    vowel_o = a.count('o')
    vowel_u = a.count('u')
    sum_vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
    return print(sum_vowels)

count_vowels('apple')  #=> 2
count_vowels('banana')  #=> 3