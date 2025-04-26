import java.util.*;

public class ProgramaTabuada {

    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        int num;
        
        System.out.print("Digite o número para fazer a tabuada: ");
        num = s.nextInt();
        
        for(int i = 0; i <=10; i++){
            
            System.out.println(num+" x "+i+" = "+ num*i);
            
        }
        
    }
    
}

