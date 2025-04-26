#include <iostream>
using namespace std;
int main()
{
	float a, b;
	cout << "Digite o primeiro numero: "; cin >> a;
	cout << "Digite o segundo numero: "; cin >> b;
	if(b==a)
		cout << "Os numeros digitados sao iguais" << endl;
	else
		cout << "Os numeros digitados sao diferentes" << endl;
	system("Pause");
}
