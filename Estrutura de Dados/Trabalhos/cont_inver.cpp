#include <stdio.h>
using namespace std;

// Fun��o para contar invers�es em um array
int countInversions(int arr[], int n) {
    int inversions = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                inversions++; // Conta uma invers�o
            }
        }
    }
    return inversions;
}

// Fun��o para verificar o estado do array
void checkArrayStatus(int arr[], int n) {
    int inversions = countInversions(arr, n); // Conta o n�mero de invers�es
    int max_inv = (n * (n - 1)) / 2; // Calcula o n�mero m�ximo de invers�es

    // Exibe o n�mero de invers�es
    printf("Inversoes: %d de %d\n", inversions, max_inv);

    // Classifica o array com base nas invers�es
    if (inversions == 0) {
        printf("O array esta completamente ordenado.\n");
    } else if (inversions > max_inv * 0.1) { // Mais de 10% de invers�es
        printf("O array esta completamente desordenado.\n");
    } else {
        printf("O array esta quase ordenado.\n");
    }
}

int main() {
    int arr1[] = {1, 2, 3, 4, 5}; // Completamente ordenado
    int arr2[] = {1, 3, 2, 4, 5}; // Quase ordenado
    int arr3[] = {5, 4, 3, 2, 1}; // Completamente desordenado

    printf("Array 1: ");
    checkArrayStatus(arr1, sizeof(arr1) / sizeof(arr1[0])); // Verifica o primeiro array

    printf("\nArray 2: ");
    checkArrayStatus(arr2, sizeof(arr2) / sizeof(arr2[0])); // Verifica o segundo array

    printf("\nArray 3: ");
    checkArrayStatus(arr3, sizeof(arr3) / sizeof(arr3[0])); // Verifica o terceiro array

    return 0;
}

