import java.util.*;

public class ProgramaCor {
	
	public static void main(String[] args) {
		   
		Random r = new Random();
		    
		String cores[] = {"azul", "vermelho", "amarelo", "roxo", "verde", "laranja", "marrom"};
		
		int pos = r.nextInt(7);
		
		String corSorteada = cores[pos];
		
		Scanner teclado = new Scanner (System.in);
		
		System.out.print("Digite uma cor: ");
		String corEscolhida = teclado.nextLine();
		
		if(corEscolhida.equals(corSorteada)){
			System.out.println("Parabéns!\nA cor realmente era "+corSorteada+".");
		}else{
			System.out.println("Você errou!\nA cor era "+corSorteada+".");
		}
	}
}