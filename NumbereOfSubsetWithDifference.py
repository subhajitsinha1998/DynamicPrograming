'''Number of possible partition a set into two subsets such that the difference of subset sums is equal to a given number.
Given a set of integers, the task is to find the number of possible way to divide it into two sets S1 and S2 such that the absolute difference between their sums is equal to a given number.'''


#Function to find the number of subsets with its sum equal to agiven positive number
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


def numberOfSubsetWithDifference(arr, difference):

    #Find the total sum of the array
    totalSum = sum(arr)

    #S1 + S2 = totalSum and S2 - S1 = difference
    #solving above two we get S1 = (totalSum - difference) / 2

    #Check if (totalSum - difference) is even
    if (totalSum - difference) % 2 == 0:

        #Find the sum of subset with smaller sum
        S1 = (totalSum - difference) // 2

        #Return the number of subset with sum S1
        return subsetSumCount(arr, S1)

    #If the subset sum is not integer return 0
    return 0


if __name__ == "__main__":
    
    array = list(map(int, input('Enter the numbers seperated by spaces: ').split(' ')))
    difference = int(input('Enter the difference to check for: '))

    print(numberOfSubsetWithDifference(array, difference))