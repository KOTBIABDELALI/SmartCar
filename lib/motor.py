import RPi.GPIO as GPIO, time

GPIO.setwarnings(False)

# Pins L1, L2 Left Motor
# Pins R1, R2 Right Motor
L1 = 16
L2 = 18
R1 = 13
R2 = 15

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(R1, GPIO.OUT)
    GPIO.setup(R2, GPIO.OUT)

def cleanup():
    stop()
    time.sleep(1)
    GPIO.cleanup()

def stop():
    GPIO.output(L1,False)
    GPIO.output(L2,False)
    GPIO.output(R1,False)
    GPIO.output(R2,False)
    
def forward():
    GPIO.output(L1,False)
    GPIO.output(L2,True)
    GPIO.output(R1,True)
    GPIO.output(R2,False)
    
def reverse():
    GPIO.output(L1,False)
    GPIO.output(L2,True)
    GPIO.output(R1,False)
    GPIO.output(R2,True)

def spinLeft():
    GPIO.output(L1,True)
    GPIO.output(L2,False)
    GPIO.output(R1,False)
    GPIO.output(R2,True)
    
def spinRight():
    GPIO.output(L1,True)
    GPIO.output(L2,False)
    GPIO.output(R1,True)
    GPIO.output(R2,False)