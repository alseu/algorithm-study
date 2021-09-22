import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;

class third {

	public static void main(String[] args) {
		String numbers = "012";
		
		//string to arraylist
		ArrayList<String> arr = new ArrayList<>();
		String[] arr1 = numbers.split("");
		for (String num : arr1)
			arr.add(num);

		//permutation result
		ArrayList<String> result = new ArrayList<>();
		//Deduplication permutation result by hashset
		HashSet<Integer> result2 = new HashSet<Integer>();

		//find all permutation by recursive
		reculsion(arr, result, result2, arr.size());

		System.out.println(result2.toString());
		
		int answer = 0;
        while(result2.iterator().hasNext()){
            int a = result2.iterator().next();
            result2.remove(a);
            if(a==2) answer++;
            if(a%2!=0 && isPrime(a)){
            	//System.out.println(a);
            	answer++;
            }
        }
		//System.out.println(answer);        
	}


	private static void reculsion(ArrayList<String> arr, ArrayList<String> result, HashSet<Integer> result2, int n) {
		if (n == 0) {

			return;
		}

		for (int i = 0; i < n; i++) {
			result.add(arr.remove(i));
			//System.out.println("||"+result.toString());
			
			String tmp = "";
			for (int j = 0; j < result.size(); j++) {
				tmp += result.get(j);
			}
			result2.add(Integer.parseInt(tmp));
			
			reculsion(arr, result, result2, n - 1);
			arr.add(i, result.remove(result.size() - 1));
			//System.out.println(";;"+arr.toString());
			//System.out.println(i+"==============");
		}                      
		//System.out.println("--------------");
	}
	
    public static boolean isPrime(int n){ 
        if(n==0 || n==1) return false;
        for(int i=2; i<(int)Math.sqrt(n)+1; i++){
            if(n%i==0) return false;
        }
        return true;
    }
}