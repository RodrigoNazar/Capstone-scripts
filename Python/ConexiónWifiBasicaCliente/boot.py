# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
# esp.osdebug(None)
import uos
import machine
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
# webrepl.start()
gc.collect()


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('\nConnecting to network...')
        sta_if.active(True)
        sta_if.connect('iPhone de Rodrigo', 'patricio')
        while not sta_if.isconnected():
            pass
    print('\nConnected!\n')


do_connect()
