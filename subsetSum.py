'''find the subsets whose sume is equal to a given positive number'''


def subsetSum(arr, sum):

    t = [[{'state':None, 'subset':[]} for _ in range(sum + 1)] for _ in range(len(arr) + 1)]
    allSubset = []

    for i in range(len(arr) + 1):
        for j in range(sum + 1):
            if j == 0:
                t[i][j]['state'] = True
                t[i][j]['subset'] = []
            elif i == 0:
                t[i][j]['state'] = False
                t[i][j]['subset'] = []
            elif arr[i - 1] <= j:
                t[i][j]['state'] = t[i - 1][j - arr[i - 1]]['state'] or t[i - 1][j]['state']
                if t[i - 1][j - arr[i - 1]]['state']:
                    t[i][j]['subset'] += t[i - 1][j - arr[i - 1]]['subset'] + [arr[i - 1]]
                if t[i - 1][j]['state']:
                    t[i][j]['subset'] += t[i - 1][j]['subset']
            else:
                t[i][j]['state'] = t[i - 1][j]['state']
                t[i][j]['subset'] += (t[i - 1][j]['subset'])
    
    temp = 0
    subset = []
    for i in t[len(arr)][sum]['subset']:
        temp += i
        subset.append(i)
        if temp == sum:
            temp = 0
            allSubset.append(subset)
            subset = []
    
    return allSubset


if __name__ == "__main__" :

    array = list(map(int, input('Enter the numbers seperated by spaces: ').split(' ')))
    sum = int(input('Enter the sum to check for: '))
    
    print(subsetSum(array, sum))