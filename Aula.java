package exemplo1;

import java.util.*;

public class Aula {
	public static void main(String[]args){
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Digite o primeiro número: ");
		int n1 = teclado.nextInt();
		
		System.out.print("Digite o segundo número: ");
		int n2 = teclado.nextInt();

		int sum = n1+n2;
		int sub = n1-n2;
		int mult = n1*n2;
		int div = n1/n2;

		System.out.println("A soma entre "+n1+" e "+n2+" é: "+sum);
		System.out.println("A subtração entre "+n1+" e "+n2+" é: "+sub);
		System.out.println("A multiplicação entre "+n1+" e "+n2+" é: "+mult);
		System.out.println("A divisão entre "+n1+" e "+n2+" é: "+div);
		
	}
}

