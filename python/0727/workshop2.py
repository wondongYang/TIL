# 소대소대

def low_and_up(a):
    list_words = []
    for i in range(0, len(a)):
        if (i+1) % 2 != 0:
            list_word = a[i]
            lower_word = list_word.lower()
            list_words.append(lower_word)
        else:
            list_word = a[i]
            upper_word = list_word.upper()
            list_words.append(upper_word)
    return print(*list_words)



low_and_up('apple') #=> aPpLe
low_and_up('banana') #=> bAnAnA