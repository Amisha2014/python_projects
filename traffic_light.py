import time

def traffic_light():
    while True:
        print (" Red Light: Stop")
        time.sleep(10)
        print(" Yellow Light: Get Ready")
        time.sleep(5)
        print(" Green Light: Go")
        time.sleep(15)

traffic_light()
