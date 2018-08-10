import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"
ser.open()
ser.write(b"hello")
