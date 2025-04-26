import java.util.*;

public class ProgramaVogaisConsoantes {

	public static void main(String[] args) {
	   
		Scanner teclado = new Scanner(System.in);
		    
		System.out.print("Digite uma palavra: ");
		String palavra = teclado.nextLine();
		
		int i = 0, consoante = 0, vogal = 0;
		
		while(i < palavra.length()){
			if(palavra.charAt(i) == 'a' || palavra.charAt(i) == 'e' || palavra.charAt(i) == 'i' || palavra.charAt(i) == 'o' || palavra.charAt(i) == 'u'){
				vogal++;
			}else{
				consoante++;
			}
			i++;
		}
		
		System.out.println("Palavra: "+palavra+"\nLetras: "+(vogal+consoante)+"\nVogal(ais): "+vogal+"\nConsoante(s): "+consoante);    
	}
}