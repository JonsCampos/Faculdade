import java.util.*;
class Carro {
    String chassi;
    String placa;
    String cor;
    String marca;
    String modelo;
    Integer ano;
    
    public Carro(){
        Scanner teclado = new Scanner(System.in);
        System.out.print("Chassi: ");
        chassi = teclado.nextLine();
        System.out.print("Placa: ");
        placa = teclado.nextLine();
        System.out.print("Cor: ");
        cor = teclado.nextLine();
        System.out.print("Marca: ");
        marca = teclado.nextLine();
        System.out.print("Modelo: ");
        modelo = teclado.nextLine();
        System.out.print("Ano: ");
        ano = teclado.nextInt();
    }
    
    public void acelerar(){
        System.out.println(this.marca + " " + this.modelo + " esta acelerando...");
    }
    
    public void freiar(){
        System.out.println(this.marca + " " + this.modelo + " esta freiando...");
    }
    
    public void buzinar(){
        System.out.println(this.marca + " " + this.modelo + " esta buzinando...");
    }
    
    public static void main(String[] args) {
        System.out.println("Digite as informacoes do primeiro carro");
        Carro c1 = new Carro();
        System.out.println("");
        c1.acelerar();
        c1.freiar();
        
        System.out.println("\nDigite as informacoes do segundo carro");
        Carro c2 = new Carro();
        System.out.println("");
        c2.buzinar();
        c2.acelerar();
    }
}