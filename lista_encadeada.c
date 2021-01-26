#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <stdbool.h>

//Definição da lista
struct celula {
	int conteudo;
	struct celula *prox;
};

//Declaração da lista
typedef struct celula Celula;

main(){
	Celula *lista;	
	lista = malloc(sizeof(Celula));
	lista->prox = NULL;
	int i;
	srand(time(NULL));
	inserir_no_inicio(2,lista);
	inserir_no_inicio(10,lista);
	inserir_no_inicio(5,lista);
	inserir_no_inicio(1,lista);
	mostrar(lista);
}

void inserir_no_inicio(int x, Celula *ini){
	Celula *nova;
	nova =  malloc(sizeof(Celula));
	nova->conteudo = x;
	nova->prox = ini->prox;
	ini->prox = nova;
}

void mostrar(Celula *lista){
	
	bool have_element = true;
	Celula *aux;
	
	aux = lista->prox;
	
	while(have_element){
				
		printf("| %i | => ",aux->conteudo);
						
		if(aux->prox == NULL){
			have_element = false;
			printf("List end");
		}
		else {
			aux = aux->prox;
		}
	}
	
}
