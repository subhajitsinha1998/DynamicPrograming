'''Unbounded Knapsack (Repetition of items allowed)
    Given a knapsack weight W and a set of n items with certain value and weight , we need to 
    calculate minimum amount that could make up this quantity exactly.'''


def unboundedKnapsack(value, weight, capacity):

    t = [[None] * (capacity + 1)] * (len(value) + 1)

    for i in range(len(value) + 1):
        for j in range(capacity + 1):
            if j == 0:
                t[i][j] = 1
            elif i == 0:
                t[i][j] = 0
            elif weight[i - 1] <= j:
                t[i][j] = max(value[i - 1] + t[i][j - weight[i - 1]], t[i - 1][j])
            else:
                t[i][j] =t[i - 1][j]

    return t[len(value)][capacity]


if __name__ == "__main__":
    
    values = list(map(int, input('Enter the values seperated by spaces: ').split(' ')))
    weights = list(map(int, input('Enter the weights seperated by spaces: ').split(' ')))
    capacity = int(input('Enter the capacity of the knapsack: '))

    print(unboundedKnapsack(values, weights, capacity))