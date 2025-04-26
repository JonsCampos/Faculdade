#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */


struct aluno
{
   char nomeAl[31], disc[21];
   int matric, tel;
   float AV1, AV2, AV3, Media;
   int turma;
};


int main() {
	
	aluno Alunos[2];
	int i;
	float MedGeral=0;
	for(i=0;i<2;i++)
	{
		cout<<"Digite os dados do aluno:"<<endl;
		cout<<"Turma: "; cin>>Alunos[i].turma;
		cout<<"Nome: "; cin>>Alunos[i].nomeAl;
		cout<<"Matricula: "; cin>>Alunos[i].matric;
		cout<<"Tefone: "; cin>>Alunos[i].tel;
		cout<<"Disciplina: "; cin>>Alunos[i].disc;
		cout<<"Nota AV1: "; cin>>Alunos[i].AV1;
		cout<<"Nota AV2: "; cin>>Alunos[i].AV2;
		cout<<"Nota AV3: "; cin>>Alunos[i].AV3;
		Alunos[i].Media = (Alunos[i].AV1 + Alunos[i].AV2+Alunos[i].AV3)/3;
		
	}
	
	for(i=0; i<2;i++)
    {
       MedGeral = MedGeral + Alunos[i].Media;   	
	} 	
	
	MedGeral = MedGeral/2;
	cout<<"Media geral : "<< MedGeral<<endl; 
	
	system("pause");
	return 0;
}