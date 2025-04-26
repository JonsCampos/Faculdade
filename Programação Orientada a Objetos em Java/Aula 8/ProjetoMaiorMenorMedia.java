import javax.swing.JOptionPane;

public class ProjetoMaiorMenorMedia {

    public static void main(String[] args) {
        
        double numero[] = {0, 0, 0, 0, 0};
        double maior = 0, menor = 0, soma = 0, media = 0;
        
        for(int i = 0; i < 5; i++){
            numero[i] = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite o "+(i+1)+"º número"));
            soma = numero[i] + soma;
            
            if(i == 0){
                menor = numero[i];
            }
                
            if(maior < numero[i]){
                maior = numero[i];
            }
            
            else if(menor > numero[i]){
                menor = numero[i];
            }
    }
        
        media = soma/5;   
        
        JOptionPane.showMessageDialog(null, "A média dos números é: "+media+"\nO maior número é: "+maior+"\nO menor número é: "+menor+".");
        
    }
    
}
