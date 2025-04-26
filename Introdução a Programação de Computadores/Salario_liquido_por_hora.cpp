#include <iostream>
using namespace std;
int main(void)
{
	float HT, VH, PD, TD, SB, SL;
	cout << "Entre com a quantidade de horas trabalhadas: "; cin >> HT;
	cout << "Entre com o valor da hora de trabalho......: "; cin >> VH;
	cout << "Entre com o valor do percentual de desconto: "; cin >> PD;
	SB = HT*VH;
	TD = (PD/100)*SB;
	SL = SB-TD;
	cout << "O Salario Bruto..:  " << SB << endl;
	cout << "Desconto.........:  " << TD << endl;
	cout << "O Salario Liquido:  " << SL << endl;
	system("Pause");
	return 0;
}
