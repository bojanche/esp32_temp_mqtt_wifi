import time
import machine
import dht
import gc

d=dht.DHT11(machine.Pin(16))
while True:
    try:
        if gc.mem_free()<102000:
            gc.collect()
        d.measure()
        print(d.temperature())
        time.sleep(2)
    except:
        pass