#include <iostream>
#include <cstdlib>
#include <cstring>
#define TAM 5

using namespace std;
struct atende
{ 
   char identificacao[TAM][60]; 
   long long notaFiscal[TAM];
   int codigoSaida[TAM], topo;  
};

void empilha(atende &pilha);
void desempilha(atende &pilha);
void mostraTopo(atende &pilha);
void lista(atende &pilha);

int main()
{
  int op;  atende carros;  
  carros.topo=-1;  
  do
   { system("cls");
    cout<<"\nPILHA( LIFO- Last In - First Out )\n\n";
    cout<<"\n1- Inserir carro";
    cout<<"\n2- Remover carro";
    cout<<"\n3- Mostrar o primeiro carro a sair";
    cout<<"\n4- listar - QUESTAO DIDATICA. Remova depois que testar";    
    cout<<"\n5- Sai";  
    cout<<"\nOpcao: ";
    cin>>op;
    system("cls");
    switch(op)
	  { 
	     case 1: cin.get(); empilha(carros);  break;
	              
	     case 2:  desempilha(carros);  break;
	              
	     case 3: mostraTopo(carros);  break;
	
	     case 4: lista(carros);  break;     
	     
	     case 5: cout<<"\nAplicacao da PILHA\n";  break;
	             
	     default: cout<<"\nOPCAO INVALIDA\n";  
	} 
	   cout<<"\n\n";system("pause"); 
   }while(op!=5);
}

void empilha(atende &pilha)
{
   char id[60];   long long nf;   int codS;
   if(pilha.topo == TAM-1)
     cout<<"\nATENCAO. Carreta  Cheia\n";
   else
   {  cout<<"\nProprietatio/ Tipo de carro/ Destino:";
       cin.getline(id, 60);
       cout<<"\nNota Fiscal: "; cin>>nf;
       cout<<"\nCodigo de saida: "; cin>>codS;       
       pilha.topo++; //atualiza o topo
       // pilha recebe valor
       strcpy(pilha.identificacao[pilha.topo], id);
       pilha.notaFiscal[pilha.topo]=nf;
       pilha.codigoSaida[pilha.topo]=codS;
   }
}

void desempilha(atende &pilha)
{
   if(pilha.topo == -1)
      cout<<"\nATENCAO. Carreta Vazia \n";
   else
   { 
     cout<<"\nCodigo do carro entregue: "; 
     cout<< pilha.codigoSaida[pilha.topo]; 
     cout<<"\nNota fiscal do carro entregue:";
     cout<< pilha.notaFiscal[pilha.topo];
     cout<<"\nIdentificacao do carro entregue: "; 
     cout<< pilha.identificacao[pilha.topo];     
     pilha.topo--;  //atualiza o topo 
   }
}


void mostraTopo(atende &pilha)
{  
   if(pilha.topo == -1)
        cout<<"\nATENCAO. Carreta Vazia \n";
   else
   {
    cout<<"\nCodigo do carro: "; 
    cout<<pilha.codigoSaida[pilha.topo];
    cout<<"\nNota fiscal do carro: ";     cout<<pilha.notaFiscal[pilha.topo];
    cout<<"\nIdentificacao do carro: "; 
    cout<<pilha.identificacao[pilha.topo];
   }   
}  


void lista(atende &pilha)
{
   if(pilha.topo == -1)
     cout<<"\nATENCAO. Carreta Vazia \n";
   else
   {  
      cout<<"\nOrdem de Saida\n";
      for(int x=pilha.topo; x>=0; x--)
     { cout<<"\n\n"<<x+1<<"o carro";
       cout<<"\nCodigo do carro: "<<pilha.codigoSaida[x];
       cout<<"\nNota fiscal do carro: "<<pilha.notaFiscal[x];
       cout<<"\nIdentificacao do carro: "; 
       cout<<pilha.identificacao[x]; 
     }
  }
} 
