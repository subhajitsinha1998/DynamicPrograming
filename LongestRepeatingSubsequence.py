


def lrs(a):

    dp = [[None] * (len(a) + 1) for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        for j in range(len(a) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == a[j - 1] and i != j:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lrs = []

    while dp[i][j] != 0:
        if a[i - 1] == a[j - 1] and i != j:
            lrs.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lrs.reverse()
    
    return dp[len(a)][len(a)], ''.join(lrs)


if __name__ == "__main__":
    
    seq = input('Enter the seuence: ')

    print(lrs(seq))