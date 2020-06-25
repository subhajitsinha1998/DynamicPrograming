


def lcs(a, b):

    dp = [[None] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])

    lcs = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1] and dp[i][j] == dp[i - 1][j - 1] + 1:
            lcs.append(a[i - 1])
            i -= 1
            j -= 1
        elif  dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()

    return [dp[len(a)][len(b)], ''.join(lcs)]


def lcps(a):
    
    return lcs(a, list(reversed(a)))


if __name__ == "__main__":
    
    str1 = input('Enter the seuence 1: ')

    print(lcps(str1))