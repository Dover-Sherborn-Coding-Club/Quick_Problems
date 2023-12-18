public class SwapVars {
	public static void main(String[] args) {
		int a = 25;
		int b = 69;
		
		a = a + b;
		b = a - b;
		a = a - b;
		
		System.out.println(a + " " + b);
		
		
	}
}
