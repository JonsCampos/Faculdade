#include <iostream>
using namespace std;
int main()
{
	float massa, vol, den;
	
	cout << "Digite a massa do material: ";
	cin >> massa;
	cout << "Digite o volume do material: ";
	cin >> vol;
	den = massa/vol;
	cout << "A densidade do material sera " << den << endl;
	system("Pause");
}
