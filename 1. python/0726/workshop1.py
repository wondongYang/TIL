def get_dict_avg(a):
    sum_a = 0
    for key in a:
        sum_a += a[key]
    return print(sum_a/len(a))
        


get_dict_avg({
    'python': 80,
    'algorithm': 90,
    'django': 89,
    'web': 83,
})