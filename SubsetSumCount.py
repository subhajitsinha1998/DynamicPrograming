'''Count the number of subset whose sume is equal to a given positive number'''


def subsetSumCount(arr, sum):
    
    t = [[None for _ in range(sum + 1)] for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        for j in range(sum + 1):
            if j == 0:
                t[i][j] = 1
            elif i == 0:
                t[i][j] = 0
            elif arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[len(arr)][sum]


if __name__ == "__main__" :

    array = list(map(int, input('Enter the numbers seperated by spaces:').split(' ')))
    sum = int(input('Enter the sum to check:'))

    print(subsetSumCount(array, sum))