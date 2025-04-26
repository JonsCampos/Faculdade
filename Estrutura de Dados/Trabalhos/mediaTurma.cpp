#include <iostream>
using namespace std;

int main(int argc, char** argv){
	char vetnome[20][10];
	float vetnotas[20][4], mediaturma = 0;
	int i, j;
	
	for (i=0; i<20; i++){
		cout << "Digite o nome do "<< (i+1) << "* aluno: ";
		cin >> vetnome[i];
		vetnotas[i][3] = 0;
		for (j=0; j<3; j++){
			cout << "Digite a " << (j+1) << "* nota de "<< vetnome[i] << ": ";
			cin >> vetnotas[i][j];
			vetnotas[i][3] += vetnotas[i][j];
		}
		cout << "\n";
		vetnotas[i][3] /= 3;
		mediaturma += vetnotas[i][3];
	}
	mediaturma /= 20;
	cout << "A media da turma e " << mediaturma << "\n\n";
	
 system("pause");	 
 return 0;
}

