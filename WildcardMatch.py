def isMatch(s: str, p: str) -> bool:
    m = len(s);
    flag = False
    if p == s:
        return True
    else:
        for i in range(len(s)-1):
            if p[i] == s[i] or p[i] == '?':
                print(p[i], s[i])
                continue
            elif p[i] == '*':
                if i < len(p) - 1:
                    j = i + 1;
                    n = i
                    print('before while' , m, i)
                    while (n <= m):
                        print(p[j], s[n])
                        if p[j] == s[n]:
                            print(('').join(s[:n + 1]))
                            i = n + 1
                            print(i)
                            flag = 'True'
                            break
                        else:
                            print('in else,' + s[n])
                            n += 1
                            print(n, m, i)
                else:
                        flag = 'True'
            else:
                print('flag2,' + flag + " " + s[i])
                flag = 'False'
    print('flagend' + flag)
    if flag == 'True':
        return True
    else:
        return False

print(isMatch("aceb","a*b"))


