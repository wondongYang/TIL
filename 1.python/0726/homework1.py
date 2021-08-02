def count_vowels(a):
    vowel_a = a.count('a')
    vowel_e = a.count('e')
    vowel_i = a.count('i')
    vowel_o = a.count('o')
    vowel_u = a.count('u')
    sum_vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
    return print(sum_vowels)

count_vowels('apple')
count_vowels('banana')