#include <stdio.h>
#include <math.h>

int main(){
	float raio, area;
	
	printf("Digite o raio do circulo: ");
	scanf("%f", &raio);
	
	area = M_PI*pow(raio,2);
	
	printf("A area do circulo e: %.2f", area);
	
	return 0;
}
