package programafuncionario;
import java.util.*;

class Funcionario{
	
	public String nome;
	public String cargo;
	public String idade;
	protected String matricula;
	protected String salario;

	public Funcionario(){		   
	}
	
	public Funcionario(String nome, String cargo, String idade, String matricula, String salario){	
	    this.nome = nome;
	    this.cargo = cargo;
	    this.idade = idade;
	    this.salario = salario;
	    this.matricula = matricula;	    
	}
	
	public void informarIdade(){
	    System.out.println("O funcionário "+this.nome+" tem "+this.idade+" anos de idade");
	}
	public void informarCargo(){
		System.out.println("O cargo do funcionário "+this.nome+" é "+this.cargo);
	}
	public void informarMatricula(){
	    System.out.println("A matrícula do funcionário "+this.nome+" é "+this.matricula);
	}
	public void receberSalario(){
	    System.out.println("O funcionário "+this.nome+" acaba de pegar o seu salário de R$"+this.salario);
	}                
}

public class ProgramaFuncionario {
    
    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        String nome , cargo, idade, matricula, salario;
        
        //Funcionário 1
        
        Funcionario f1 = new Funcionario();
                
        System.out.print("Informe o nome do 1º funcionário: ");
        nome = teclado.nextLine();
        f1.nome = nome;

        System.out.print("Informe o cargo do 1º funcionário: ");
        cargo = teclado.nextLine();
        f1.cargo = cargo;
        
        System.out.print("Informe a idade do 1º funcionário: ");
        idade = teclado.nextLine();
        f1.idade = idade;
        
        System.out.print("Informe a matrícula do 1º funcionário: ");
        matricula = teclado.nextLine();
        f1.matricula = matricula;
        
        System.out.print("Informe o salario do 1º funcionário: ");
        salario = teclado.nextLine();
        f1.salario = salario;

        
        //Funcionário 2
        
        System.out.print("\nInforme o nome do 2º funcionário: ");
        nome = teclado.nextLine();

        System.out.print("Informe o cargo do 2º funcionário: ");
        cargo = teclado.nextLine();
        
        System.out.print("Informe a idade do 2º funcionário: ");
        idade = teclado.nextLine();
        
        System.out.print("Informe a matrícula do 2º funcionário: ");
        matricula = teclado.nextLine();
        
        System.out.print("Informe o salario do 2º funcionário: ");
        salario = teclado.nextLine(); 
        
        Funcionario f2 = new Funcionario(nome , cargo, idade, matricula, salario); 

        
        //Funcionário 3
        
        System.out.print("\nInforme o nome do 3º funcionário: ");
        nome = teclado.nextLine();

        System.out.print("Informe o cargo do 3º funcionário: ");
        cargo = teclado.nextLine();
        
        System.out.print("Informe a idade do 3º funcionário: ");
        idade = teclado.nextLine();
        
        System.out.print("Informe a matrícula do 3º funcionário: ");
        matricula = teclado.nextLine();
        
        System.out.print("Informe o salario do 3º funcionário: ");
        salario = teclado.nextLine();
        
        Funcionario f3 = new Funcionario(nome , cargo, idade, matricula, salario);

        
        System.out.println("");
        f1.informarIdade();
        
        System.out.println("");
        f2.informarMatricula();
        
        System.out.println("");
        f3.receberSalario();
    }  
}
