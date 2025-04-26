#include <stdio.h>
using namespace std;

// Função para mesclar (merge) dois subarrays
// O primeiro subarray é arr[l..m]
// O segundo subarray é arr[m+1..r]
void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1; // Tamanho do primeiro subarray
    int n2 = r - m;     // Tamanho do segundo subarray

    // Arrays temporários para armazenar os valores a serem mesclados
    int L[n1], R[n2];

    // Copiando os dados para os arrays temporários L[] e R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int i = 0; i < n2; i++)
        R[i] = arr[m + 1 + i];

    // Índices iniciais dos subarrays L[] e R[]
    int i = 0, j = 0;

    // Índice inicial do subarray mesclado
    int k = l;

    // Comparar e mesclar os dois subarrays
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {    // Se o elemento em L é menor ou igual ao de R
            arr[k] = L[i];     // Coloca L[i] na posição correta de arr
            i++;               // Move para o próximo elemento de L
        } else {
            arr[k] = R[j];     // Caso contrário, coloca R[j] em arr
            j++;               // Move para o próximo elemento de R
        }
        k++;                   // Avança o índice no array original
    }

    // Copia os elementos restantes de L[], se houver
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copia os elementos restantes de R[], se houver
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Função recursiva que implementa o Merge Sort
// arr[]: array a ser ordenado
// l: índice inicial
// r: índice final
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;  // Calcula o ponto médio

        // Chama mergeSort recursivamente para as duas metades
        mergeSort(arr, l, m);     // Metade esquerda
        mergeSort(arr, m + 1, r); // Metade direita

        // Mescla as duas metades ordenadas
        merge(arr, l, m, r);
    }
}

// Função para imprimir um array
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    // Array de exemplo para ser ordenado
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Array original: ");
    printArray(arr, n); // Imprime o array original

    mergeSort(arr, 0, n - 1); // Chama a função mergeSort para ordenar o array

    printf("Array ordenado: ");
    printArray(arr, n); // Imprime o array ordenado

    return 0;
}

