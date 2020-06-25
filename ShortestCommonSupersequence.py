'''Shortest Common Supersequence
Given two strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences.'''



def scs(a, b):

    dp = [[None] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])

    scs = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1] and dp[i][j] == dp[i - 1][j - 1] + 1:
            scs.append(a[i - 1])
            i -= 1
            j -= 1
        elif  dp[i][j] == dp[i - 1][j]:
            scs.append(a[i - 1])
            i -= 1
        else:
            scs.append(b[j - 1])
            j -= 1

    if i:
        scs.append(a[:i])
    elif j:
        scs.append(b[:j])

    scs.reverse()

    return len(a) + len(b) - dp[len(a)][len(b)], ''.join(scs)


if __name__ == "__main__":
    
    str1 = input('Enter the seuence 1: ')
    str2 = input('Enter the seuence 2: ')

    print(scs(str1, str2))