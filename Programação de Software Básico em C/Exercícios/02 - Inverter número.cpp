#include <stdio.h>

int main(){
	int num, uni, dez, cen;
	
	printf("Digite um numero de 3 digitos: ");
	scanf("%d", &num);
	
	uni = num%10;
	dez = (num/10)%10;
	cen = num/100;	
	
	printf("O numero invertido e: %d%d%d", uni,dez,cen);
	
	return 0;
}
