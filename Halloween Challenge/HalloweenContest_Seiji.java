public class HalloweenContest_Seiji {
	static String[] ghost = {
"       .-.    ",
"      | o |   ",
"    |^_.' '._|^ ",
"   |         |  ",
"    ||       |  ",
"     ||    |`   ",
"   |__|  |      ",
"   *.__.'       "};
	static int space = 0; //Space between ghost and left side of window
	
	public static void main(String[] args) throws InterruptedException {
		int counter = 15; //Integer counter to prevent infinite loop
		
		while (counter > 0)	{ //Main loop of system
			
			for (int i = 0; i < 3; i++) { //loop for ghost to go forward
				clearScreen();
				printGhost();
				space++;
				Thread.sleep(400);
			}
			flipGhost();
			
			for (int i = 0; i < 3; i++) { //loop for ghost to go backward
				clearScreen();
				printGhost();
				space--;
				Thread.sleep(400);
			}
			flipGhost();
			
			counter--;
		}
	}
	
	public static void printGhost() {
		System.out.println("  HAPPY HALLOWEEN!\n");
		
		for (String i : ghost) { //"For i in each" loop to iterate over String array "ghost"
			for (int j = space; j > 0; j--) {
				System.out.print(" ");
			}
			System.out.println(i); //Prints out each 
		}
	}
	
	public static void clearScreen() {
		for (int i = 0; i < 20; i++) {
			System.out.println(""); //Prints blank 20 times to move to next "frame"
		}
	}
	public static String reverseString(String input) { //Method to reverse current string
		String output = "";
		for (int i = input.length(); i > 0; i--) {
			output += input.charAt(i-1);
		}
		return output;
	}
	public static void flipGhost() {
		int index = 0;
		for (String i : ghost) {
			ghost[index] = reverseString(i);
			index++;
		}
	}
	
}