// Palindrome Partitioning:
// Given a string, a partitioning of the string is a palindrome partitioning 
// if every substring of the partition is a palindrome.


import java.util.Scanner;

public class PalimdromicPartition {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        System.out.print("Enter the string: ");
        String s = in.nextLine();
        System.out.println(solve(s));
        in.close();

    }

    static Boolean isPalindrom(String a){
        if (a.substring((int)Math.ceil((double)a.length()/2)).equals(new StringBuilder(a.substring(0,a.length()/2)).reverse().toString())) {
            return(true);
        } else {
            return(false);
        }
    }

    static int solve(String a){

        int dp[][] = new int[a.length()][a.length()];

        for (int diff = 0; diff < dp.length; diff++) {
            for (int i = 0; i < dp.length - diff; i++) {
                int j = i + diff;
                if (i == j || isPalindrom(a.substring(i, j + 1))) {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = Integer.MAX_VALUE;
                    for (int k = i; k < j; k++) {
                        dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k + 1][j] + 1);
                    }
                }
            }
        }
        return(dp[0][a.length() - 1]);
    }
}