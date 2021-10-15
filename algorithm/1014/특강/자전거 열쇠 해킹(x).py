def key():
    for i in range(10):
        password = []
        if password[0] != 7 and password[0] != 8:
            return
        else:
            password[0] = i
            for j in range(10):
                password[1] = j
                for k in range(10):
                    if password[2] != 1 and password[2] != 2 and password[2] != 7 and password[2] != 9:
                        return
                    else:
                        password[2] = k
                        for t in range(10):
                            password[3] = t
                            print(*password)
                            password.pop()
                    if password[2] == 1 or password[2] == 2 or password[2] == 7 or password[2] == 9:
                        password.pop()
                password.pop()
            if password[0] == 7 or password[0] == 8:
                password.pop()
                
N = 4
key()
