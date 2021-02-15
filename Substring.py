def test(s):
    matched = []
    # print(s)
    for ch in s:
        print('start :' + str(matched))
        if ch in matched:
            print(' duplicate: ' + ch)
            break
        else:
            matched= (' ').join(ch)
            print(matched)
    print(matched)



print(test('cass'))