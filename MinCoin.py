


def minCoin(coins, sum):

    t = [[None] * (sum + 1)] * (len(coins) + 1)

    for i in range(len(coins) + 1):
        for j in range(sum + 1):
            if i == 0:
                t[i][j] = float('inf')
            elif j == 0:
                t[i][j] = 0
            elif coins[i - 1] <= j:
                t[i][j] = min(t[i][j - coins[i - 1]] + 1, t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]

    coinsUsed = []

    while j > 0:
        if t[i][j] - 1 == t[i][j - coins[i - 1]]:
            coinsUsed.append(coins[i - 1])
            j -= coins[i - 1]
        else:
            i -= 1

    return [t[len(coins)][sum], coinsUsed]


if __name__ == "__main__":

    coins = list(map(int, input('Enter the values of the coins seperated by spaces: ').split(' ')))
    sum = int(input('Enter the sum to find: '))

    minCoins, coinsUsed = minCoin(coins, sum)

    print('Minimum number of coins required are:',minCoins)
    print('Coins used are:',coinsUsed)