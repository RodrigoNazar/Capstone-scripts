import uos
import machine
import gc
gc.collect()


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('iPhone de Rodrigo', 'patricio')
        while not sta_if.isconnected():
            pass


do_connect()
