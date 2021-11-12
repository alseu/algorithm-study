package algo1;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class twoPlusOne {

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numTests = sc.nextInt();

        Integer[] goodsCost = new Integer[numTests];
        int min_cost = 0;
        
        for(int i = 0; i < numTests; i++) {
            goodsCost[i]=sc.nextInt();
        }
        Arrays.sort(goodsCost,Collections.reverseOrder());

        for(int i = 0; i < numTests; i++) {
        	if(i%3 != 2)
        		min_cost += goodsCost[i];
        	
//            System.out.print(i);
        }
        System.out.print(min_cost);
        
        
    }


}
