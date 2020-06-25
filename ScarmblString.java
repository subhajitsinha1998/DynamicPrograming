import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


// Scramble String
// Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
// Below is one possible representation of s1 = "great":

//     great
//    /    \
//   gr    eat
//  / \    /  \
// g   r  e   at
//            / \
//           a   t
// To scramble the string, we may choose any non-leaf node and swap its two children.
// For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

//     rgeat
//    /    \
//   rg    eat
//  / \    /  \
// r   g  e   at
//            / \
//           a   t
// We say that "rgeat" is a scrambled string of "great".


public class ScarmblString {
    public static void main(String[] args) {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        try {

            System.out.println(isScrambleString(in.readLine(), in.readLine()));
            in.close();

        } catch (IOException e) {
            System.out.println(e);
        } 
    }

    static boolean isScrambleString(String str1, String str2){
        boolean[][] dp = new boolean[str1.length()][str2.length()];

        for (int i = 0; i < str1.length(); i++) {
            for (int j = 0; j < str1.length(); j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = str1.charAt(i) == str2.charAt(i);
                } else {
                    dp[i][j] = (dp[i - 1][j - 1] && str1.charAt(i) == str2.charAt(i)) || (dp[i - 1][j] && dp[j][i - 1]);
                }
            }
        }

        System.out.println(Arrays.deepToString(dp));
        return dp[str1.length() - 1][str2.length() - 1];
    }
}