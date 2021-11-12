

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;

public class anagram {

    private static boolean solveAnagrams(String first, String second ) {
        /* ------------------- INSERT CODE HERE --------------------
         *
         * Your code should return true if the two strings are anagrams of each other.
         *
         * */

        char[] first_sort = first.toCharArray();
        char[] second_sort = second.toCharArray();
        Arrays.sort(first_sort);
        Arrays.sort(second_sort);
        
        String rst_first = String.valueOf(first_sort);
        String rst_second = String.valueOf(second_sort);
        
        if(!rst_first.equals(rst_second)) {
            return false;
        }else
            return true;
        

        /* -------------------- END OF INSERTION --------------------*/
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numTests = sc.nextInt();

        for (int i = 0; i < numTests; i++) {
            String first = sc.next().toLowerCase();
            String second = sc.next().toLowerCase();

            System.out.println(first + " & " + second + " are " + (solveAnagrams(first, second) ? "anagrams." : "NOT anagrams."));
        }
    }
}
