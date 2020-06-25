'''0-1 Knapsack Problem
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.'''


def knapsack(weight, value, knapsackWeight):

    t = [[0 for _ in range(knapsackWeight + 1)] for _ in range(len(value) + 1)]

    for i in range(len(value) + 1):
        for j in range(knapsackWeight + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif weight[i - 1] <= j:
                t[i][j] = max(value[i - 1] + t[i - 1][j - weight[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]

    return t[len(value)][knapsackWeight]


if __name__ == "__main__":

    values = list(map(int, input('Enter the values seperated by spaces:').split(' ')))
    weights = list(map(int, input('Enter the weights seperated by spaces:').split(' ')))
    capacity = int(input('Enter the capcity of knapsack:'))
    
    print('Highest value the Knapsack can hold is', knapsack(weights, values, capacity))