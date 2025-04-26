#include <iostream>
using namespace std;

struct aluno {
	char nomeAl[31], disc[21];
	int matric, tel;
	float av1, av2, av3, media;
	int turma;
};

int main(int argc, char *argv[])
{	
	int tam, i;
	float media;

	cout << "Digite a quantidade de alunos: ";
	cin >> tam;
	cout << "\n";
	
	aluno alunos[tam];
	
	for (i=0; i<tam; i++){
		cout << i+1 << "* aluno\n";
		cout << "Nome: "; cin >> alunos[i].nomeAl;
		cout << "Matricula: "; cin >> alunos[i].matric;
		cout << "Telefone: "; cin >> alunos[i].tel;
		cout << "Disciplina: "; cin >> alunos[i].disc;
		cout << "Turma: "; cin >> alunos[i].turma;
		cout << "Av1: "; cin >> alunos[i].av1;
		cout << "Av2: "; cin >> alunos[i].av2;
		cout << "Av3: "; cin >> alunos[i].av3;
		alunos[i].media = (alunos[i].av1 + alunos[i].av2 + alunos[i].av3) / 3;
		media += alunos[i].media;
		cout << "\n";
	}
	
	media /= tam;
	
	cout << "Media da turma: " << media;
	
	cout << "\n";
    system("Pause");
    return 0;
}
