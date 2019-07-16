import pypinyin

def PINYIN(string):
    a = pypinyin.pinyin(string, style=pypinyin.FIRST_LETTER)

    b = []
    for i in range(len(a)):
        b.append(str(a[i][0]).upper())
    c = ''.join(b)
    return c
