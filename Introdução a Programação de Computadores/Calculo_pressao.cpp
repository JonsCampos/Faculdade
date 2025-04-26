#include <iostream>
#include <iomanip>
using namespace std;

int main()
{ 
	float p_atm, p_pascal, v = 54.1, n = 2, r = 0.082, tc = 27, tk, equiv = 101325;
	
	cout << setiosflags(ios::scientific);
	tk = tc + 273.15;
	p_atm = ( n * r * tk ) / v;
	cout << p_atm << " atm" << endl;
	p_pascal = p_atm * equiv;
	cout << p_pascal << " pascais" << endl << endl;
	system ("pause");
	return 0;
}

