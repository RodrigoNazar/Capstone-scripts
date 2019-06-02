// Mathías Lambert V. (c) - Lab8 SEP 2018-2

#include "mi_uart.h"
#include <stdlib.h>
#include <stdint.h>


Lista* crear_lista() {
    Lista* lista = malloc(sizeof(Lista));
    lista -> numero_de_datos = 0;
    lista -> cabeza = NULL;
    return lista;
}

void agregar_nodo(Lista* lista, unsigned char letra){
    lista -> numero_de_datos++;
    Nodo* nodo = malloc(sizeof(Nodo));
    nodo -> caracter = letra;
    nodo -> siguiente = NULL;
    if (lista -> cabeza == NULL) {
        lista -> cabeza = nodo;
    }
    else {
        Nodo* aux;
        for (aux = (lista -> cabeza); aux -> siguiente != NULL; aux = (aux -> siguiente));
        aux -> siguiente = nodo;
    }
}

void pasar_string(Lista* listarx, Lista* listatx) {
    Nodo* aux;
    Nodo* aux2;
    aux = listarx -> cabeza;
    while (aux != NULL){
        agregar_nodo(listatx, aux -> caracter);
        aux2 = aux;
        aux = aux -> siguiente;
        free(aux2);
    }
    free(listarx);
    listarx = crear_lista();
}

/*char* leer_lista(Lista* lista){
    if (lista -> cabeza != NULL){
        Nodo* aux;
        char* palabra = malloc((lista -> numero_de_datos + 1) * sizeof(char));
        int i = 0;
        aux = lista -> cabeza;
        while (aux != NULL){
            palabra[i] = aux -> caracter;
            i++;
            aux = aux -> siguiente;
        }
        palabra[i] = 0x00;
        return palabra;
    }
    else {
        return "";
    }
}*/

void kill_lista(Lista* lista){
    Nodo* aux1;
    Nodo* aux2;
    aux1 = lista -> cabeza;
    while (aux1 != NULL) {
        aux2 = aux1 -> siguiente;
        free(aux1);
        aux1 = aux2;
    }
    free(lista);
}

Configuracion* crear_configuracion(uint16_t baund, int bits_paridad, int bits_mensaje, int bist_parada) {
    Configuracion* conf = malloc(sizeof(Configuracion));
    conf -> baudrate = baund;
    conf -> bits_de_paridad = bits_paridad;
    conf -> bits_de_mensaje = bits_mensaje;
    conf -> bits_de_parada = bist_parada;
    return conf;
}

void kill_configuracion(Configuracion* configuracion) {
    free(configuracion);
}

#include <avr/io.h>
#include <avr/interrupt.h>

#define F_CPU 16000000UL

void configurar_uart(Configuracion* datos) {

    uint8_t MYUBRR = F_CPU/16/(datos -> baudrate) - 1;

    /*Fijar bound rate*/
    UBRR0H = (MYUBRR >> 8);
    UBRR0L = MYUBRR;

    UCSR0B |= (1 << RXEN0) | (1 << TXEN0);      // Activar recepcion y transmision
    UCSR0B |= (1 << RXCIE0);                    // Activar interrupcion para recibir
    switch (datos -> bits_de_mensaje) {
        case 5:
            UCSR0C |= (0 << UCSZ01) | (0 << UCSZ00);  // 5data
            break;
        case 6:
            UCSR0C |= (0 << UCSZ01) | (1 << UCSZ00);  // 6data
            break;
        case 7:
            UCSR0C |= (1 << UCSZ01) | (0 << UCSZ00);  // 7data
            break;
        case 8:
            UCSR0C |= (1 << UCSZ01) | (1 << UCSZ00);  // 8data
            break;
        default:
            UCSR0C |= (1 << UCSZ01) | (1 << UCSZ00);  // 8data
            break;

    }

    if (datos -> bits_de_parada == 2) {
        UCSR0C |= (1 << USBS0);  // 2bits de parada
    }

    switch (datos -> bits_de_paridad) {
        case 1:
            UCSR0C |= (1 << UPM01) | (0 << UPM00);  // Even parity
            break;
        case 2:
            UCSR0C |= (1 << UPM01) | (1 << UPM00);  // Odd parity
            break;
        default:
            UCSR0C |= (0 << UPM01) | (0 << UPM00);  // Disabled parity
            break;
    }
}

void enviar_caracter(unsigned char caracter) {
    while(!(UCSR0A&(1<<5)));
    UDR0 = caracter;
}

void enviar_str(char* str) {
    while(*str !=0x00){
        while(!(UCSR0A&(1<<5)));
        UDR0 = *str;
        str++;
    }
}

void recibir_str(char* buffer, uint8_t bufflen) {
    char recibido;
    int c = 0;
    while(1){
        while ( !(UCSR0A & (1 << RXC0)) );
        recibido = UDR0;             // leer RX buffer
        if (c >= bufflen) {
            *buffer = 0x00;
            break;
        }
        if (recibido != 10 && recibido != 13) {
            *buffer = recibido;
        }
        else if (recibido == 10){
            *buffer = 0x00;
            break;
        }
        buffer++;
        c++;
    }
}

char recibir_char() {
    while ( !(UCSR0A & (1 << RXC0)) );
    return UDR0;
}



void leer_lista(Lista* lista){
    Nodo* aux;
    Nodo* aux2;
    aux = lista -> cabeza;
    while (aux != NULL){
        enviar_caracter(aux -> caracter);
        aux2 = aux;
        aux = aux -> siguiente;
        free(aux2);
    }
    free(lista);
}
