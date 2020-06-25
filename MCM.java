// Matrix Chain Multiplication:
// Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
// The problem is not actually to perform the multiplications, but merely to decide in which order 
// to perform the multiplications


import java.util.Arrays;
import java.util.Scanner;

class MCM{
    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        
        System.out.print("Enter the numbers seperated by spaces: ");
        String a[] = s.nextLine().split(" ");

        try{
        int[] x = Arrays.stream(a).mapToInt(Integer::parseInt).toArray();
        System.out.print(solve(x));
        }
        finally {
            s.close();
        }
    }

    static int solve(int[] arr){

        int dp[][] = new int[arr.length][arr.length];

        for (int diff = 0; diff < arr.length; diff++) {
            for (int i = 1; i < arr.length - diff; i++) {
                int j = i + diff;
                if (i == j) {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = Integer.MAX_VALUE;
                    for (int k = i; k < j; k++) {
                        dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]);
                    }
                }
            }
        }
        return(dp[1][arr.length - 1]);
    }
}