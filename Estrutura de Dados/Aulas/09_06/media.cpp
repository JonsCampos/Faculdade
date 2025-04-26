#include <iostream>
#include <cstdlib>
#define TAM 3
using namespace std;

void media(float [],float [],float [],int );
void saida(float [] ,float [],float [],int );

int main(){
	float nota1[]={7.5,8, 9},nota2[]={6.5,6,5},medias[TAM];
	
	media(nota1, nota2,medias,TAM); 
	saida(nota1,nota2,medias,TAM); 
	cout<<"\n\n";
	
	system("pause");
}

void media(float n1[],float n2[],float m[],int t){
	int x;
	
	for(x=0;x<t;x++)
	m[x]=(n1[x]+n2[x])/2; 
} 

void saida(float n1[],float n2[],float m[],int t){
	int x;
	
	system("cls");
	cout<<"\nNota 1\tNota 2\tMedia\n";
	for(x=0;x<t;x++)
	cout<<"\n"<<n1[x]<<"\t"<<n2[x]<<"\t"<<m[x]; 
}

