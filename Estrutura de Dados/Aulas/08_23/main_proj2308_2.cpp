#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

struct produto
{
  char nomeProd[21];
  int codigo;
  float valor;
};


int main(int argc, char** argv) {
	int tam, i;
	cout<< tam<< endl;
	
	cout<<"Digite o tamanho do vetor: ";
	cin>>tam;

    produto prod01[tam]; 	
	cout<< tam<< endl;
	
	for(i=0;i<tam;i++)
	{
	   cout<< "Digite o codigo do produto:";
	   cin >> prod01[i].codigo; 
	
	   cout<< "Digite o nome do produto:";
	   cin >> prod01[i].nomeProd; 
    
	   cout<< "Digite o valor do produto:";
	   cin >> prod01[i].valor; 
   }//for
	
   for(i=0;i<tam;i++)	
   {
      cout << "Codigo produto:"<<prod01[i].codigo<<"O produto digitado foi: "<< prod01[i].nomeProd<< "  Seu valor: "<< prod01[i].valor<< endl; 
    }	
	
		
    system("pause");	
	return 0;
}