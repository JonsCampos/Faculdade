#include <iostream>
using namespace std;
int main()
{
	float N1, N2, N3, N4, media;
	cout << "Nota do Primeiro Bimestre: "; cin >> N1;
	cout << "Nota do Segundo Bimestre: "; cin >> N2;
	cout << "Nota do Terceiro Bimestre: "; cin >> N3;
	cout << "Nota do Quarto Bimestre: "; cin >> N4;
	media = (N1+N2+N3+N4)/4;
	cout << "Media final = " << media << endl;
	system("Pause");
}
