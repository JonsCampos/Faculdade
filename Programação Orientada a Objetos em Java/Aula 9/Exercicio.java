import javax.swing.*;

    public class Exercicio{
        JFrame tela;
        JPanel painel;
        JLabel lblMatricula, lblNome, lblCargo, lblSalario, lblEndereco;
        JTextField txtMatricula, txtNome, txtCargo, txtSalario, txtEndereco;
        JButton btnCadastrar;
        
        public Exercicio(){
            tela = new JFrame();
            painel = new JPanel();
            lblMatricula = new JLabel("Matrícula");
            txtMatricula = new JTextField(10);
            lblNome = new JLabel("Nome");
            txtNome = new JTextField(10);
            lblCargo = new JLabel("Cargo");
            txtCargo = new JTextField(10);
            lblSalario = new JLabel("Salario");
            txtSalario = new JTextField(10);
            lblEndereco = new JLabel("Endereço");
            txtEndereco = new JTextField(10);
            
            btnCadastrar = new JButton("Cadastrar");
            
            
            tela.getContentPane().add(painel);
            painel.add(lblMatricula); painel.add(txtMatricula);
            painel.add(lblNome); painel.add(txtNome);
            painel.add(lblCargo); painel.add(txtCargo);            
            painel.add(lblSalario); painel.add(txtSalario);
            painel.add(lblEndereco); painel.add(txtEndereco);
            painel.add(btnCadastrar);
            
            tela.setSize(200, 250);
            
            
            tela.setVisible(true);
            tela.show();
            
            tela.setResizable(false);
            tela.setLocationRelativeTo(null);
            
        }
    
   
    
    public static void main(String[] args) {
        
        Exercicio ex = new Exercicio();
        
    }
    
}
