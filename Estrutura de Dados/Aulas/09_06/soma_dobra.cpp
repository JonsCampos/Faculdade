#include <iostream>
#include <cstdlib>
using namespace std;

float soma(float n); // float soma(float);
float dobra(float n); // float dobra(float); 

int main(){ 
	float num=20;
	
	cout<<"\nApos chamar a funcao soma : "<<soma(num);
	cout<<"\nApos chamar a funcao dobra: "<<dobra(num); 
	cout<<"\n\n";
	
	system("pause");
}

float soma(float n){
	return dobra(n)+5; 
}

float dobra(float n){
	return n*2;
}
