import java.util.*; 

public class ProgramaDecrescente {
 
    public static void main(String[] args) {
    
        int a, b, c;
        
        Scanner s = new Scanner(System.in);
        
        System.out.print("Digite o primeiro número: ");
        a = s.nextInt();
        
        System.out.print("Digite o segundo número: ");
        b = s.nextInt();
        
        System.out.print("Digite o terceiro número: ");
        c = s.nextInt();
        
        if(a >= b && b >= c){
            System.out.println("Os números em ordem decrescente ficam: "+a+" -> "+b+" -> "+c);
        }else if(a >= c && c >= b){
            System.out.println("Os números em ordem decrescente ficam: "+a+" -> "+c+" -> "+b);
        }else if(b >= a && a >= c){
            System.out.println("Os números em ordem decrescente ficam: "+b+" -> "+a+" -> "+c);
        }else if (b >= c && c >= a){
            System.out.println("Os números em ordem decrescente ficam: "+b+" -> "+c+" -> "+a);
        }else if(c >= a && a >= b){
            System.out.println("Os números em ordem decrescente ficam: "+c+" -> "+a+" -> "+b);
        }else if (c >= b && b >= a){
            System.out.println("Os números em ordem decrescente ficam: "+c+" -> "+b+" -> "+a);
        }else{
            System.out.println("ERRO!!!");
        }    
    }
}
