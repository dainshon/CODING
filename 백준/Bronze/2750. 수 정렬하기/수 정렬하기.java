import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);

		int count = scan.nextInt();
		int array[] = new int[count];
		
		for(int i=0;i<count;i++) {
			array[i] = scan.nextInt();
		}
		int temp;
		
		for(int i=0;i<count;i++) {
			for(int j=i+1;j<count;j++) {
				if(array[i] > array[j]) {
					temp = array[i];
					array[i] = array[j];
					array[j] = temp;
				}
			}
		}
		
		for(int i=0;i<count;i++) {
			System.out.println(array[i]);
		}
		
		scan.close();

		
	}

}

//String[] array = str.split(" "); 문자열 자르기