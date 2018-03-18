from RPi.GPIO import GPIO
GPIO.setmode(GPIO.BOARD)  # the pin numbers refer to the board connector not the chip
GPIO.setup(??, GPIO.INPUT, GPIO.PUD_UP) # set up pin ?? (one of the above listed pins) as an input with a pull-up resistor
if GPIO.input(??):
    print "switch is open"
else:
    print "switch is closed"
