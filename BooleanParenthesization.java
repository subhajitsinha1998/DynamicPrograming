import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;


// Boolean Parenthesization Problem:
// Given a boolean expression with following Symbols: 'T' ---> true ,'F' ---> false 
// And following operators filled between symbols: & --> boolean AND , | --> boolean OR , ^ --> boolean XOR 
// Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.


public class BooleanParenthesization {
    public static void main(final String[] args) {

        Scanner in = new Scanner(System.in);

        System.out.println(booleanParenthesization(in.next()));

        in.close();
    }


    static int booleanParenthesization(String a) {
        int[][] f = new int[a.length()][a.length()];
        int[][] t = new int[a.length()][a.length()];

        for (int l = 0; l < a.length(); l += 2) {
            for (int i = 0; i < a.length() - l ; i += 2) {
                int j = i + l;
                
                if(i == j ){

                    if (eval(a.substring(i, j + 1))) {
                        t[i][j] = 1;
                    } else {
                        f[i][j] = 1;
                    }

                } else{

                    for (int k = i + 1; k < j; k += 2) {
                        if(a.charAt(k) == '|'){

                            t[i][j] += t[i][k - 1] * t[k + 1][j] + t[i][k - 1] * f[k + 1][j] + f[i][k - 1] * t[k + 1][j];
                            f[i][j] += f[i][k - 1] * f[k + 1][j];

                        } else if(a.charAt(k) == '&'){

                            t[i][j] += t[i][k - 1] * t[k + 1][j];
                            f[i][j] += f[i][k - 1] * f[k + 1][j] + t[i][k - 1] * f[k + 1][j] + f[i][k - 1] * t[k + 1][j];                            

                        } else if(a.charAt(k) == '^'){

                            t[i][j] += t[i][k - 1] * f[k + 1][j] + f[i][k - 1] * t[k + 1][j];
                            f[i][j] += f[i][k - 1] * f[k + 1][j] + t[i][k - 1] * t[k + 1][j];                            

                        } else{
                            System.out.println("Enter right expression!");
                        }
                        
                    }

                }
            }
        }

        System.out.println(Arrays.deepToString(t));
        System.out.println(Arrays.deepToString(f));
        return(t[0][a.length() - 1]);
    }


    static boolean eval(String a) {

        @SuppressWarnings("serial")
        final HashMap<Character, Boolean> operand = new HashMap<Character, Boolean>() {
            {
                put('T', true);
                put('F', false);
            }
        };

        boolean temp = operand.get(a.charAt(0));

        for (int i = 1; i < a.length() - 1; i++) {
            if (a.charAt(i) == '&') {
                temp = temp & operand.get(a.charAt(i + 1));
            } else if (a.charAt(i) == '|') {
                temp = temp | operand.get(a.charAt(i + 1));
            } else if(a.charAt(i) == '^'){
                temp = temp ^ operand.get(a.charAt(i + 1));
            } else {
                continue;
            }
        }

        return(temp);

    }
}