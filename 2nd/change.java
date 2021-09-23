import java.util.Scanner;

class change {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int input = sc.nextInt();
		int case_5 = input / 5;

		while ((input - case_5 * 5) % 2 != 0) {
			case_5--;
		}

		int answer = (input - case_5 * 5) / 2 + case_5;
		System.out.println(answer);
		return;
		
	}
}