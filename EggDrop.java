import java.util.Scanner;


// Egg Dropping Puzzle 
// The following is a description of the instance of this famous puzzle involving n=2 eggs and a building 
// with k=36 floors. Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing. We make a few assumptions:

// …..An egg that survives a fall can be used again.
// …..A broken egg must be discarded.
// …..The effect of a fall is the same for all eggs.
// …..If an egg breaks when dropped, then it would break if dropped from a higher floor.
// …..If an egg survives a fall then it would survive a shorter fall.
// …..It is not ruled out that the first-floor windows break eggs, nor is it ruled out that 
//     the 36th-floor do not cause an egg to break.
// If only one egg is available and we wish to be sure of obtaining the right result, the experiment 
// can be carried out in only one way. Drop the egg from the first-floor window; if it survives, 
// drop it from the second-floor window. Continue upward until it breaks. In the worst case, 
// this method may require 36 droppings. Suppose 2 eggs are available. What is the least number of 
// egg-droppings that is guaranteed to work in all cases?


public class EggDrop {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        System.out.print("Enter the number of floors and eggs seperated by spaces: ");
        System.out.println("Min. no. of attempts is : " + eggDrop(in.nextInt(), in.nextInt()));

        in.close();
    }


    static int eggDrop(int floor, int egg){

        int[][] dp = new int[egg + 1][floor + 1];

        for (int i = 1; i <= egg; i++) {
            for (int j = 1; j <= floor; j++) {
                if (i == 1) {
                    dp[i][j] = j;
                } else {
                    dp[i][j] = Integer.MAX_VALUE;
                    for (int k = 1; k <= j; k ++) {
                        dp[i][j] = Math.min(dp[i][j], 1 + Math.max(dp[i - 1][k - 1], dp[i][j - k]));
                    }
                }
            }
        }

        return(dp[egg][floor]);
    }
}