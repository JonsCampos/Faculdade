package exemplo3;

import java.util.*;

public class Aula3_1 {
	public static void main(String[]args) {
		
		Scanner teclado = new Scanner(System.in);
		
		int cont = 0;
		for (int i = 0; i < 10; i++) {
			System.out.printf("Digite a idade da %dª pessoa: ", i+1);
			int idade = teclado.nextInt();
			if (idade < 18) {
				cont += 1;
			}
		}
		
		if (cont == 1) {
			System.out.printf("%d pessoa tem idade menor que 18", cont);
		}else {
			System.out.printf("%d pessoas tem idade menor que 18", cont);
		}
	}
}
