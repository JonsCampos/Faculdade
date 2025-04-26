#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

struct Aluno 
{
   char nome[20];
   float media ;
   	
};

int main(int argc, char** argv) {
  int tamT, i;
  Aluno vetAlu[tamT];
  float mediaTurma=0; 
  
  cout<<"Digite o tamanho da turma:";
  cin>>tamT;
   
  for(i=0;i<tamT;i++)
  {  
    cout<<"Digite o nome do aluno:";
    cin>>vetAlu[i].nome;
    
    cout<<"Digite a media do aluno:";
    cin>>vetAlu[i].media;
    
    mediaTurma = mediaTurma + vetAlu[i].media;
  
  }  
  
  
 cout<< "Media geral da turma foi:"<<mediaTurma;  
 
 system("pause");	 
 return 0;
}