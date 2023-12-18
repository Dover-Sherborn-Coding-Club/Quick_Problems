/**
 * This is the CollatzConjecture modeled in java
 */
public class CollatzConjecture {

	public static void main(String[] args) {	
		System.out.print(collatz(123));
	}
	public static int collatz(int x) {
		int y = 1;
		while(x != 1) {
			if (x % 2 == 0) {
				x /= 2;
				y++;
			} else {
				x = 3*x+1;
				y++;
			}
		}
		return y;
	}

}
