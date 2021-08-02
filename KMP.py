def compute_lps_array(arr):
    lps = [0] * len(arr)
    lps[0] = 0
    i = 1
    length = 0
    while i < len(arr):
        if arr[i] != arr[length]:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        else:
            length += 1
            lps[i] = length
            i += 1

    return lps


def kmp_string(string, pattern):
    lps = compute_lps_array(pattern)

    i = 0
    j = 0
    while i < len(string):
        if pattern[j] == string[i]:
            i += 1
            j += 1

        if j == len(pattern):
            print('Found ' + pattern + ' at ' + str(i-j))
            j = lps[j - 1]

        elif i < len(string) and pattern[j] != string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


string = 'UIGHIUQGUYAABAACAABAAGSYOUHQIUHUI'
pattern = 'AABAACAABAA'
kmp_string(string, pattern)
