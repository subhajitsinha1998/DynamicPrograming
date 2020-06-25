'''Partition a set into two subsets such that the difference of subset sums is minimum.
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.'''


#This function returns the list of all the sum of all subset possible
def subsetSum(arr):

    totalSum = sum(arr)
    
    t = [[None for _ in range(totalSum + 1)] for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        for j in range(totalSum + 1):
            if j == 0:
                t[i][j] = True
            elif i == 0:
                t[i][j] = False
            elif arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    subsetSums = []

    for j in range(totalSum + 1):
        if t[len(arr)][j]:
            subsetSums.append(j)

    return subsetSums


def minSubsetSumDifference(arr):

    #Find all the sum of subsets possible
    subsetSums = subsetSum(arr)

    #Find upper bound of sum of subsets
    range = sum(arr)

    #Initialize min difference as sum of subsets at upper bound
    minDiff = range

    #The difference of two subset wis sum of lower one as s1 is (range - s1)
    #Try to minimize (range - 2s1) using the lower half of all subset sums
    for s1 in subsetSums[0:len(subsetSums)//2 + 1]:
        minDiff = min(minDiff, abs(range - 2 * s1))

    #Return the value of min difference possible
    return minDiff


if __name__ == "__main__" :

    array = list(map(int, input('Enter the numbers seperated by spaces:').split(' ')))
    
    print(minSubsetSumDifference(array))