package algo1;

import java.util.Scanner;

public class fibo2 {

	public static void main(String[] args) {
		long[] arr;

		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		arr = new long[n + 1];
		arr[0] = 0;
		arr[1] = 1;
		
		System.out.println(fibo(arr, n));
	}

	public static long fibo(long[] arr, int n) {
		if (arr[n] ==0 && n != 0) {
			arr[n] = fibo(arr, n - 1) + fibo(arr ,n - 2);
		}
		return arr[n];
	}
}
