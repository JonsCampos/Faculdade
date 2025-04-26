#include <iostream>
using namespace std;
int main()
{
	float a;
	cout << "Digite o numero: "; cin >> a;
	if(a==0)
		cout << "O numero digitado e nulo" << endl;
	else if(a>0)
		cout << "O numero digitado e positivo" << endl;
	else
		cout << "O numero digitado e negativo" << endl;
	system("Pause");
}
