import javax.swing.*;
import java.awt.event.*;
import java.util.*;

public class MegaSena implements ActionListener{

    JFrame tela;
    JPanel painel;
    JLabel lblTexto;
    JButton btnJogar;
    
    public MegaSena(){
     
        tela = new JFrame();
        painel = new JPanel();
        lblTexto = new JLabel("Mega Sena de Java");
        btnJogar = new JButton("Jogar");
        btnJogar.addActionListener(this);
        
        tela.getContentPane().add(painel);
        
        painel.add(lblTexto);
        painel.add(btnJogar);
        
        tela.setSize(200,100);
        tela.setVisible(true);
        tela.show();
        
    }
    
    public static void main(String[] args) {
        MegaSena ms = new MegaSena();
    }
    
    public void actionPerformed(ActionEvent e){ 
        
      Random r = new Random();
      int n[] = new int[6];
      
      for(int i = 0; i < 6; i++){
          int x = r.nextInt(1, 61);
          n[i] = x;
      }
      
      JOptionPane.showMessageDialog(null, "Os números são: " + n[0] + ", " + n[1] + ", " + n[2] + ", " + 
              n[3] + ", " + n[4] + ", " + n[5]);
    }
    
}
