import java.util.*;

public class ProgramaCaloria{
 
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        
        int cal = 0;
        
        System.out.print("Digite o prato que deseja: ");
        String prato = s.nextLine();
        
        System.out.print("Digite a sobremesa que deseja: ");
        String sobremesa = s.nextLine();
        
        System.out.print("Digite a bebida que deseja: ");
        String bebida = s.nextLine();
        
        switch(prato){
            
            case "vegetariano":
                cal += 180;
                break;
                
            case "peixe":
                cal += 230;
                break;

            case "frango":
                cal +=250;
                break;
            
            case "carne":
                cal +=350;
                break;
                
            default:
                System.out.println("Erro!");
        }
        
        switch(sobremesa){
            
            case "abacaxi":
                cal += 75;
                break;
            
            case "sorvete diet":
                cal += 110;
                break;
                
            case "mousse diet":
                cal += 170;
                break;
                
            case "mousse de chocolate":
                cal += 200;
                break;
                
            default:
                System.out.println("Erro!");
        }
        
        switch(bebida){
            
            case "cha":
                cal += 20;
                break;
                
            case "suco de laranja":
                cal += 70;
                break;
            
            case "suco de melao":
                cal += 100;
                break;
                
            case "refrigerante diet":
                cal += 65;
                break;
            
            default:
                System.out.println("Erro!");
        }
        System.out.println("O total de calorias é: "+cal);
    }
    
}
