import random
import time

# meetinterval in seconden
INTERVAL = 3

def lees_temperatuur():
    return round(random.uniform(18, 24), 1)

def lees_vochtigheid():
    return random.randint(30, 60)

for _ in range(3):
    print("Temperatuur:", lees_temperatuur(), "Vochtigheid:", lees_vochtigheid())
    time.sleep(INTERVAL)
