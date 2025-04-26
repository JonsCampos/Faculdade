#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

void msgRecebe(char msg[ ]);

int main(){
	char str[] ="ESTRUTURA DE DADOS";
	
	msgRecebe(str); cout<<"\nDepois da funcao: "<<str<< endl;
	
	system("pause > NULL");
}

void msgRecebe(char msg[ ]){
	int tam= strlen(msg); 
	
	msg[0]='*';
	cout<<"\n"<<msg<< " tem "<< tam<< " caracteres\n";
}

