#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>
#include <avr/interrupt.h>
#include "./libreria/mi_uart.h"
#define F_CPU 16000000UL
#define MAX 200
#define MIN 41


unsigned char recibido;

//char msj[10];


enum accion{
    Motor_derecho,
    Motor_izquierdo,
    Motor_arriba,
    Motor_abajo,
    Ambos_longitudinal,
    Ambos_transversal,
    Todos,
    Nada
}; typedef enum accion Accion;

Accion accion_actual;

int main(){
    //estado_echo = PIND & (1 << 3);
    //int distancia;
    accion_actual = Nada;

    /*DDRD |= (1 << PD2);*/

    /*
    DDRB |= (1 << DDB1)|(1 << DDB2);
    // PB1 and PB2 is now an output, is D9 and D10

    ICR1 = 333;
    // set TOP to 333

    OCR1A = MAX;
    OCR1B = MAX;

    TCCR1A |= (1 << COM1A1)|(1 << COM1B1);
    TCCR1B |= (1 << WGM13) | (1 << CS10);
    */

    DDRD |= (1 << DDD6) | (1 << DDD5);
    // PD6 asd PD5 is now an output
    OCR0A = MAX;
    OCR0B = MAX;
    TCCR0A |= (1 << COM0A1) | (1 << COM0B1);
    TCCR0A |=  (1 << WGM00);
    TCCR0B |= (1 << CS00);

    DDRB |= (1 << DDB3);
    DDRD |= (1 << DDD3);
    // PB3 asd PD3 is now an output
    OCR2A = MAX;
    OCR2B = MAX;
    TCCR2A |= (1 << COM2A1) | (1 << COM2B1);
    TCCR2A |= (1 << WGM20);
    TCCR2B |= (1 << CS20);
    // set prescaler to 8 and starts PWM


    Configuracion* conf = crear_configuracion(57600, 0, 8, 1);
    configurar_uart(conf);
    kill_configuracion(conf);
    sei();

    while(1){}
}


void calibrar(void){
    for(volatile uint16_t i = MAX - 1; i > MIN; i--){
        /*OCR1A = i;
        OCR1B = i;*/
        OCR0A = i;
        OCR0B = i;
        OCR2A = i;
        OCR2B = i;
    }
}


ISR (USART_RX_vect) {
    recibido = UDR0;
    /*sprintf(msj, "%d\n", recibido);
    enviar_str(msj);
    enviar_caracter(recibido);*/

    if (recibido == 0) {
        calibrar();
    }
    /*else {
        OCR0A = recibido;
        OCR0B = recibido;
        OCR2A = recibido;
        OCR2B = recibido;
    }*/
    else if (recibido == 1){
        accion_actual = Motor_derecho;
    }
    else if (recibido == 2){
        accion_actual = Motor_izquierdo;
    }
    else if (recibido == 3){
        accion_actual = Motor_arriba;
    }
    else if (recibido == 4){
        accion_actual = Motor_abajo;
    }
    else if (recibido == 5){
        accion_actual = Ambos_longitudinal;
    }
    else if (recibido == 6){
        accion_actual = Ambos_transversal;
    }
    else if (recibido == 7){
        accion_actual = Todos;
    }
    else if (recibido > MIN && recibido < MAX) {
        switch (accion_actual) {
            case Motor_izquierdo:
                OCR0A = recibido;
                break;
            case Motor_derecho:
                OCR0B = recibido;
                break;
            case Motor_arriba:
                OCR2B = recibido;
                break;
            case Motor_abajo:
                OCR2A = recibido;
                break;
            case Ambos_transversal:
                OCR2A = recibido;
                OCR2B = recibido;
                break;
            case Ambos_longitudinal:
                OCR0A = recibido;
                OCR0B = recibido;
                break;
            case Todos:
                OCR0A = recibido;
                OCR0B = recibido;
                OCR2A = recibido;
                OCR2B = recibido;
                break;
        }
        accion_actual = Nada;
    }
}
