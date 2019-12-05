#include <stdio.h>

int main(int argc, char const *argv[])
{

	int i = 0b010101; // 0b000001

	printf("%d\n", i);

	// i = i << 1;
	// Shift para la izquierda = 0b000100
	// Si se pasa, le mete un dígito significativo al coso

	// i = ~i;

	i &= ((1 << 2) | (1 << 6));

	/*

		Set bit:

	PORTB = 8;
	PORTB |= (1 << 2);

	Expandido:

	  0000 1000     PORTB (set to 8 on the first line)
	| 0000 0100     mask (created with (1<<2) )
	 ----------
	  0000 1100     result, loaded into PORTB

	*/

	/*

		Clear bit:

	PORTC = 34;
	PORTC &= ~(1 << 5);

	Expandido:

		0010 0010     PORTC (set to 34 on the first line)
  	  & 1101 1111     mask (created with (1<<5) )
       ----------
        0000 0010     result, loaded into PORTC

	*/

	/*

		Flip bit:

	PORTD = 8;
	PORTD ^= (1 << 3);

	Expandido:

		0000 1000     PORTD (set to 8 on the first line)
	 ^  0000 1000     mask (created with (1<<5) )
        ----------
        0010 0000     result, loaded into PORTD

	*/

	/*

		Get bit:

	PORTD = 8;
	PORTD &= (1 << 3);

	Expandido:

		0000 1000     PORTB (set to 8 on the first line)
	 &  0000 1000     mask (created with (1<<3) )
        ----------
    	0000 1000     result > 0 therefore the 3rd bit is set(1)

	*/

	/* 

		Chequear el estado de un registro:

	if (SREG & (1 << N) > 0)
	{
    	// some code here
	}

	*/

	/*

	Para na salida digitar de un micro, se puede conectar un resistor y un diodo hacia:
		- Vcc, para accionar este led basta con setear el pin de output a GND (sinking output)
		- GND, para accionar este led basta con setear el pin de output a Vcc (Sourcing output)

		Es mejor el sinking, las componentes circuitales a veces no tienen suficiente corriente para suministrar (muchas veces limitada)
	*/

	/*
		Teoría de operación Output:

	DDxn	PORTxn 	PUD	I/O	Pull-up	Comentarios
	0		0		x	in	no
	0		1		0	in	si
	0		1		1	in	no
	1		0		x	out	no		Output-low (sink)
	1		1		x	out	no		Output-high (source)

	x in {A, B, C, D} -> El puerto que estamos usando
	n in {1, 2, 3, 4, ...} -> El número del pin

	#include <avr/io.h>


	int main(void)
	{
		DDRD |= (1 << DDD0);        // sets bit DDD0 to 1 within register DDRD
		// PD0 is now an output WOOT !!!

		PORTD |= (1 << PORTD0);     // turn on PD0
		// PD0 is now an output and is sourcing VCC

		PORTD &= ~(1 << PORTD0);     // turn off PD0
		// PDO is still an output and is now sinking 0V

		while(1)
		{
			// main loop   
		}
	}

	*/

	/*
		Teoría de operación de Inputs:

	Voltajes menores a .2V son registrados como LOW y mayores a .6V son como HIGH

	Si tenemos un botón conectado al pin, cuando el botón no esté presionado,
	el nodo queda flotando.

	Para leer el valor que está en el pin, hay que leer el registro PINx
	con x in {1, 2, 3, ...}

	Notemos que como tenemos el pullup resistor, el registro estará con entradas
	altas todo el tiempo (0b11111111) y si se registra un valor a GND, el bit de ese
	pin estará en 0.

	Es por esto que para verificar si un pin está abajo, se dice (PINB & (1<<PINB5)) == 0

	// this code sets PB5 to an input with a pull-up enable

	#include <avr/io.h>

	int main(void)
	{
		DDRB &= ~(1 << DDB5); // Clear the PB5 pin
		// PB5 is now an input

		PORTB |= (1 << PORTB5); // turn On the Pull-up
		// PB5 is now an input with pull-up enabled


		while (1)
		{
			if( (PINB & (1<<PINB5)) == 0)
			{ 
				// do something when PD5 is on
			}

				if( (PIND & (1<<PIND0)) > 0)
			{
				// do something if PD0 is off
			}

			// DEBOUBCE DE SOFTWARE

			if( (PIND & (1<<PIND0)) == 0)    //is the pin set
			{ 
				_delay_ms(25); //wait a 25ms
				if( (PIND & (1<<PIND0)) == 0) // is the pin still set
				{
					// do something because its a valid input
				}
				else
				{
					// do nothing because the input is invalid
				}
			}
		}
	}

	¿Cuando no se necesitará un pullup?
	Cuando la entrada venga de otro servicio donde el pin estará solo en GND o Vcc

	*/

	/*
		Interrupts:

	Los vectores de interrupción vienen en orden, el cual indica el orden en el que se irán
	ejecutando si es que hace más de una rutina de interrupción.

	Los interrupts se activan con la función sei() -> set interrupts
	Los interrupts se desactivan con la función cli() -> clear interrupts

	#include <avr/io.h>

	#include <avr/interrupt.h>

	volatile uint8_t test;


	int main(void)
	{
		sei();         //enable interrupts

		while (1)      // main loop
		{

			// code here can be interrupted 

			cli();     // turn off interrupts

			// all code executed here cannot be interrupted 

			sei();     // enable interrupt

			// code here can be interrupted 

			;
		}
	}



	ISR (INT0_vect)    // INT0 interrupt function
	{
		// enter code to execute here 
	}



	ISR (BADISR_vect)  // special function, to execute if a bad interrupt is called
	{
		// enter code to execute here 
	}

	ISR(***_vect) es la función que se ejecutará cuanto el vector *** es llamado. 
	Y *** es una condición que da el datasheet

	volatile uint8_t test;
	Es una variable que permitirá ser usada y updateada por la interrupción de manera 
	satisfactoria, porque el compilador no optimizará el código omitiendo cosas.
	*/

	/*
		External Interrupt:

	Las interrupciones pueden ser gatilladas por cuatro distintas situaciones:
		- Cuando se registra un voltaje LOW en el pin.
		- Cuando se registra un cambio de HIGH a LOW en un pin o viceversa
		- Cuando se registra un flanco de subida 
		- Cuando se registra un flanco de bajada

	Las interrupciones externas utilizan 3 registros:
		- EICRA: External Interrupt Control Register A, que setea la forma en la que se gatillará la interrupción
		- EIMSK: Habilita el uso de la interrupción externa en el pin INTx
		- EIFR: Ni idea

	#include <avr/io.h>
	#include <avr/interrupt.h>


	int main(void)
	{
		DDRD &= ~(1 << DDD2);     // Clear the PD2 pin
		// PD2 (PCINT0 pin) is now an input

		PORTD |= (1 << PORTD2);    // turn On the Pull-up
		// PD2 is now an input with pull-up enabled



		EICRA |= (1 << ISC00);    // set INT0 to trigger on ANY logic change
		EIMSK |= (1 << INT0);     // Turns on INT0

		sei();                    // turn on interrupts

		while(1)
		{
			// main program loop here 
		}
	}



	ISR (INT0_vect)
	{
		// interrupt code here 
	}


	*/

	/*
		Pin Change Interrupt:
	
	Hay placas que traen sus propios pines con sus propios vectores de interrupción (external interrupt)
	pero hay otros micros que no, estos conparten el vector de interrupción y se debe diferenciar via código
	que pin causará la interrupción.

	En la atmega328p se tienen sólo dos pines con external interrupt, pero todos los demas son Change Interrupt
	Se requieren más pasos lógicos para poder setear un pin change interrupt, pero es muy parecido al External
	Interrupt

	*/

	/*
		Timer - Counter

	Teoría de Operación:

	Cuando la unidad lógica de control recibe un pulso desde el preescalador, se incrementa (o decrementa) en una
	unidad el registro TCNTn. Luego, el registro TCNTn se compara con el registro OCRn.

	Cuando el registro TCNTn obtiene el mismo (o superior o menor) valor que el registro OCRn, la unidad lógica de control
	limpia lo que hay en el registro TCNTn y activa el bit de TOVn (time overflow), el cual se mantiene activo hasta que es
	reseteado por el mismo usuario.

	El registro TCNTn puede volver a 0 luego del overflow o puede comenzar a contar hacia abajo.

	Preescalador:

	Divide el numero de pulsos de entrada, contando una cantidad de pulsos y cuando llega hasta el numero seteado, genera un pulso propio
	que hace que se cuente el tiempo finalmente.


	*/

	/*
		Timers:

	OCRn =  [ (clock_speed / Prescaler_value) * Desired_time_in_Seconds ] - 1


	Normal mode:
	Mas o menos, por que no es confiable para cosas que tengan que pasar cada cierto tiempo

	CTC mode:

	When the prescaler receives a pulse from a clock cycle and passes it onto the Control Logic.  The Control Logic increments the TCNTn register by 1.  The TCNTn register is compared to the OCRn register, when a compare match occurs the TOVn bit is set in the TIFR register.

	Cuando ocurre el overflow TOVn puede generar un timer overflow interrupt (con los respectivos registros para activar la interrupción)

	Registros importantes:

	- Preescalado
	- Activado de interrupción
	- Modo del Timer	

	// this code sets up a timer0 for 4ms @ 16Mhz clock cycle
	// an interrupt is triggered each time the interval occurs.



	#include <avr/io.h> 
	#include <avr/interrupt.h>


	int main(void)
	{

		// Set the Timer Mode to CTC
		TCCR0A |= (1 << WGM01);

		// Set the value that you want to count to
		OCR0A = 0xF9;

		TIMSK0 |= (1 << OCIE0A);    //Set the ISR COMPA vect

		sei();         //enable interrupts


		TCCR0B |= (1 << CS02);
		// set prescaler to 256 and start the timer


		while (1)
		{
			//main loop
		}
	}


	ISR (TIMER0_COMPA_vect)  // timer0 overflow interrupt
	{
		//event to be exicuted every 4ms here
	}


	Los pasos:
	- Modo del Timer
	- Número al que se contará
	- Setear la interrupción a la comparación
	- El preescalado

	*/

	/*
		Contadores:

	#include <avr/io.h>
	#include <avr/interrupt.h>



	int main(void)
	{
		DDRD &= ~(1 << DDD4);     // Clear the PD4 pin
		// PD0 is now an input

		PORTD |= (1 << PORTD4);   // turn On the Pull-up
		// PDO is now an input with pull-up enabled

		TIMSK0 |= (1 << TOIE0);    // enable timer interrupt

		TCCR0B |= (1 << CS02) | (1 << CS01) | (1 << CS00);
		// Turn on the counter, Clock on Risf

		sei();                    // enable Interrupts


		while (1)
		{
			// we can read the value of TCNT0 hurray !!
		}
	}


	ISR (TIMER0_OVF_vect)
	{
		// interrupt just fired
	}

	*/

	/*
		PWM:

	Duty_Cycle = [ON_time / (ON_time + OFF_time) ] * 100 
	Output_Voltage = Duty_Cycle * Input_Voltage

	Aquí el preescalado del timer o counter aparece para controlar la frecuencia a la que se genera la señal.


	Fast PWM mode:

	Con el contador, osea: clock -> Preescalador -> Unidad de control -> Registro contador
	-> overflow? -> Generador de Onda OCFnx pin

	Es de alta frecuencia y se usa para DAC, LEDs, rectificación y regulación de potencia.

	PWM_fequency = clock_speed / [Prescaller_value * (1 + TOP_Value) ]


	Phase Corrected PWM mode:

	Cuenta hasta arriba y luego cuenta hacia abajo
	Updatea el tope cuando se llega al máximo

	PWM_frequency = clock_speed / (2 * Prescaller_value * TOP_value )


	Phase and Frequency Corrected:

	Updatea el tope una vez llega al mínimo

	PWM_frequency = clock_speed / (2 * Prescaller_value * TOP_value )


	*/

	/*
		Analog Inputs:

	A veces se tienen varias entradas que pueden tomar entradas analógicas, pero
	sólo 1 adc conectado a un solo multiplexor.

	El número de bits de un ADC indica cuantas separaciones (resolución) puede tener
	una señal (5v -> 5V/2**10 ~~ .005V de resolución)

	Reference Voltage Source:

	Voltaje máximo de referencia in {2V to Vcc}

	ADC Multiplexer Source:

	Multiplexor que elegirá a que pin sensar con el ADC

	ADC Data Register Control:

	Como la AVR es un micro de 8 bits, y el adc es de 10, tenemos que separar el número que leemos
	del ADC en dos (trabajar con registros de 16 bits) o también podemos botar los últimos 2 bits menos significativos
	Esto se puede setear desde un registro

	ADC Conversion Timing:

	A que frecuencia estará tomando muestras


	Modes of Operation:

	Single Conversion -> Toma una muestra y estamo
	La gracia es que sirve para trabajar con varios pines a la vez, sólo cambiando el multiplexor
	Lo malo es que el procesador se queda esperando el valor del ADC mientras este adquiere la muestra y la procesa

	Free Running -> Una vez que se toma una muestra, ya se está calculando la siguiente


	ADC Interrupt: 

	// this code scans ADC1 for an analog signal upon request, using 8Mhz processor clock

	#include <avr/io.h>
	#include <stdint.h>       // needed for uint8_t


	int ADCsingleREAD(uint8_t adctouse)
	{
		int ADCval;

		ADMUX = adctouse;         // use #1 ADC
		ADMUX |= (1 << REFS0);    // use AVcc as the reference
		ADMUX &= ~(1 << ADLAR);   // clear for 10 bit resolution
		
		ADCSRA |= (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);    // 128 prescale for 8Mhz
		ADCSRA |= (1 << ADEN);    // Enable the ADC

		ADCSRA |= (1 << ADSC);    // Start the ADC conversion

		while(ADCSRA & (1 << ADSC));      // Thanks T, this line waits for the ADC to finish 


		ADCval = ADCL;
		ADCval = (ADCH << 8) + ADCval;    // ADCH is read so ADC can be updated again

		return ADCval;
	}

		

	int main(void)
	{
		int ADCvalue;

		while (1)
		{
				ADCvalue = ADCsingleREAD(1);
				// ADCvalue now contains an 10bit ADC read
		}
	}

	Pasos:
	- Elige que ADC usar
	- Elige la referencia
	- Resolución
	- Preescalado del clock
	- Activa el ADC
	- Comienza la conversión
	- Espera a que la conversión termine


	*/

	/* 
		UART:

	Baud rate: 9600 
	Data bits: 8 
	Parity: None 
	Stop Bit: 1 
	Flow Control: None

	Factores:
	-Transmitting Speed
	-

	// This code waits for a character and transmits the character back (with interrupts)
 

	#include <avr/io.h>
	#include <stdint.h>                     // needed for uint8_t

	#include <avr/interrupt.h>


	#define FOSC 16000000                       // Clock Speed
	#define BAUD 9600                
	#define MYUBRR FOSC/16/BAUD -1


	volatile char ReceivedChar;


	int main( void )
	{
		// Set baud rate 
		UBRRH = (MYUBRR >> 8);
		UBRRL = MYUBRR;
		
		UCSRB |= (1 << RXEN) | (1 << TXEN);      // Enable receiver and transmitter
		UCSRB |= (1 << RXCIE);                   // Enable the receiver interrupt
		UCSRC |= (1 << URSEL) |(1 << UCSZ1) | (1 << UCSZ0);    // Set frame: 8data, 1 stp


		sei();

		
		while(1)
		{
		;                                    // main loop
		}    
	}


	ISR (USART_RXC_vect)
	{
		ReceivedChar = UDR;                     // Read data from the RX buffer
		UDR = ReceivedChar;                     // Write the data to the TX buffer

	}


	*/

	/*
		SPI:

	SCK
	MISO
	MOSI
	SS

	*/

	printf("%d\n", i);

	return 0;
}
