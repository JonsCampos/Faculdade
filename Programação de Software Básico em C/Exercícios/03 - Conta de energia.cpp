#include <stdio.h>

int main(){
	float kwh, cons, conta;
	
	printf("Digite o valor do kWh: ");
	scanf("%f", &kwh);
	
	printf("Digite o valor do consumo: ");
	scanf("%f", &cons);
	
	conta = kwh*cons;
	
	printf("O valor da conta e: R$%.2f", conta);
	
	return 0;
}
