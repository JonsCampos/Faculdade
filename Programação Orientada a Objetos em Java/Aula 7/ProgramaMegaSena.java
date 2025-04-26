import java.util.*;

public class ProgramaMegaSena {

    public static void main(String[] args) {
			
		Random r = new Random();
		  
		int numeros[] = new int[6];
		  
		for(int i = 0; i < 6; i++){
			int x = r.nextInt(60) + 1;
			numeros[i] = x;
		}
		  
		System.out.print("Os números são: ");
		  
		for(int i = 0; i < 6; i++){
			System.out.print(numeros[i]+" ");
		}
    }
}
