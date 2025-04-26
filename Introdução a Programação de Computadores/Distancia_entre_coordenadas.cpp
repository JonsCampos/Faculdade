#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	float x1, y1, x2, y2, d;
	cout << "Digite X do ponto P: "; cin >> x1;
	cout << "Digite Y do ponto P: "; cin >> y1;
	cout << "Digite X do ponto Q: "; cin >> x2;
	cout << "Digite Y do ponto Q: "; cin >> y2;
	d = sqrt(pow((x2-x1),2)+pow((y2-y1),2));
	cout << "Distancia entre pontos = " << d << endl;
	system("Pause");
}
