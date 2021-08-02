def last_occur(pattern_str, text):
    char_set = set(text)
    L = {}
    for char in char_set:
        try:
            L[char] = pattern_str.rindex(char)
        except:
            L[char] = -1

    return L


def boyer_moore(text, pattern_str):
    L = last_occur(pattern_str, text)
    j = len(P) - 1
    i = j
    m = len(P)
    loop = 0
    while i < len(T):
        loop += 1
        if T[i] == P[j]:
            if j == 0:
                return True, loop, i
            i = i - 1
            j = j - 1
        else:
            i = i + m - min(j, 1 + L[T[i]])
            j = m - 1
    return False


if __name__ == '__main__':
    T = 'abacaabadcabacabaabb'
    P = 'abacab'
    # T = 'an toan'
    # P = 'oan'
    print(boyer_moore(T, P))
