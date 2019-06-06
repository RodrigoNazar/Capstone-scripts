#include <avr/io.h>
#include <stdlib.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "./libreria/mi_uart.h"
#define F_CPU 16000000UL
#define MAX 255
#define MIN 41
#define TRIGGER_ON() PORTD |= (1 << PD2)
#define TRIGGER_OFF() PORTD &= ~(1 << PD2)

char recibido;
//char m[15];
/*
int tiempo_espera;
int espera;
char estado_echo;*/

enum accion{
    Motor_derecho,
    Motor_izquierdo,
    Ambos,
    Nada
}; typedef enum accion Accion;

Accion accion_actual;

int main(){
    //estado_echo = PIND & (1 << 3);
    //int distancia;
    accion_actual = Nada;

    /*DDRD |= (1 << PD2);*/

    DDRB |= (1 << DDB1)|(1 << DDB2);
    // PB1 and PB2 is now an output, is D9 and D10

    ICR1 = 333;
    // set TOP to 333

    OCR1A = MAX;
    OCR1B = MAX;

    TCCR1A |= (1 << COM1A1)|(1 << COM1B1);
    TCCR1B |= (1 << WGM13) | (1 << CS10);

    /* Timer 0 para contar tiempo
       modo comparación, cuenta hasta 16 para freq 1us
       prescaler 1*/
    /*TCCR0A |= (1 << WGM01);
    OCR0A = 16;
    TCCR0B |= (1 << CS01);

    // Interruptor echo
    DDRD &= ~(1 << 3);
    //PORTD |= (1 << 3);
    PCMSK2 |= (1 << 3);
    PCICR |= (1 << 2);*/

    Configuracion* conf = crear_configuracion(57600, 0, 8, 1);
    configurar_uart(conf);
    kill_configuracion(conf);
    sei();

    while(1){
        /*enviar_str("aii\n");
        TRIGGER_OFF();
        _delay_us(5);

        TRIGGER_ON();
        _delay_us(10);

        TRIGGER_OFF();
        //TIMSK0 |= (1 << OCIE0A);
        //while(!(PIND&ECHO));
        //tiempo_espera = 0;
        //while((PIND&ECHO));
        //TIMSK0 &= ~(1 << OCIE0A);
        espera = 1;
        while(espera);

        distancia = tiempo_espera * 10 / 292/ 2;
        _delay_ms(1000);*/

    }
}


void calibrar(void){
    for(volatile uint16_t i = MAX - 1; i > MIN; i--){
        OCR1A = i;
        OCR1B = i;
    }
}


ISR (USART_RX_vect) {
    recibido = UDR0;
    /*sprintf(m, "%c\n", recibido);
    enviar_str(m);*/
    if (recibido == 0) {
        calibrar();
    }
    else if (recibido == 3){
        accion_actual = Motor_derecho;
    }
    else if (recibido == 4){
        accion_actual = Motor_izquierdo;
    }
    else if (recibido == 5){
        accion_actual = Ambos;
    }
    else if (recibido > MIN && recibido < MAX) {
        switch (accion_actual) {
            case Motor_izquierdo:
                OCR1A = recibido;
                break;
            case Motor_derecho:
                OCR1B = recibido;
                break;
            case Ambos:
                OCR1A = recibido;
                OCR1B = recibido;
                break;
        }
        accion_actual = Nada;
    }
}

/*
ISR (TIMER0_COMPA_vect) {
    tiempo_espera++;
}



ISR(PCINT2_vect){
    char leer = PIND & (1 << 3);
    if (leer != estado_echo) {
        if (leer == 0) {
            TIMSK0 &= ~(1 << OCIE0A);
            espera = 0;
            sprintf(m, "%d i\n", tiempo_espera);
            enviar_str(m);
        }
        else if (leer == 1) {
            TIMSK0 |= (1 << OCIE0A);
            tiempo_espera = 0;
        }
    }
    estado_echo = PIND & (1 << 3);
}
*/
