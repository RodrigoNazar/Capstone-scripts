#include <avr/io.h>
#include <stdint.h>
#include "./libreria/mi_uart.h"
#define F_CPU 16000000UL
#define MAX 170
#define MIN 35

int main(){
    char m[5];

    DDRB |= (1 << DDB1)|(1 << DDB2);
    // PB1 and PB2 is now an output, is D9 and D10

    ICR1 = 333;
    // set TOP to 333

    OCR1A = MAX;
    OCR1B = MAX;

    TCCR1A |= (1 << COM1A1)|(1 << COM1B1);

    TCCR1B |= (1 << WGM13) | (1 << CS10);

    Configuracion* conf = crear_configuracion(57600, 0, 8, 1);
    configurar_uart(conf);
    kill_configuracion(conf);

    enviar_str("Conecte los motores\n");
    for(volatile uint32_t i = 0; i < 1600000; i++);
    for(volatile uint32_t i = 0; i < 1600000; i++);
    enviar_str("Comenzando calibracion\n");

    for(volatile uint16_t i = MAX - 1; i > MIN; i--){
        OCR1A = i;
        OCR1B = i;
    }
    enviar_str("Listo\n");
    for(volatile uint32_t i = 0; i < 1600000; i++);
    enviar_str("Empezando\n");

    while(1){
        for(volatile uint16_t i = MIN+1; i < MAX; i++){
            OCR1A = i;
            OCR1B = i;
            sprintf(m, "%d\n", i);
            enviar_str(m);
            for(volatile uint32_t i = 0; i < 320000; i++){}
        }
        OCR1A = MIN;
        OCR1B = MIN;
        for(volatile uint32_t i = 0; i < 1600000; i++);

    }
}
