


def lcs(a, b):

    dp = [[None] * (len(b) + 1) for _ in range(len(a) + 1)]
    lcs = 0
    x, y = 0, 0

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0 or j == 0 or a[i - 1] != b[j - 1]:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                lcs = max(lcs, dp[i][j])
                if lcs == dp[i][j]:
                    x, y = i, j

    i, j = x, y
    s = []

    while dp[i][j] > 0:
        s.append(a[i - 1])
        i -= 1
        j -= 1

    s.reverse()

    return lcs, ''.join(s)


if __name__ == "__main__":
    
    str1 = input('Enter the seuence 1: ')
    str2 = input('Enter the seuence 2: ')

    print(lcs(str1, str2))