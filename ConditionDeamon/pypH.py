import time
import serial
ser = serial.Serial(
		port='/dev/ttyUSB0',
		baudrate=9600,
		parity=serial.PARITY_ODD,
		stopbits=serial.STOPBITS_TWO,
		bytesize=serial.SEVENBITS
)

ser.isOpen()


print "Activating continuous reading" 
ser.write('C,1\r')
time.sleep(1)

def readbuffer(ser):
        out = ''
	cnt=0
	tmp=""
        while (ser.inWaiting() > 0 )| (tmp!='\r'):
                tmp =  ser.read(1)
		out += tmp
		cnt+=1
        return out


def readpH():
	# configure the serial connections (the parameters differs on the device you are connecting to)
	ser = serial.Serial(
		port='/dev/ttyUSB0',
		baudrate=9600,
		parity=serial.PARITY_ODD,
		stopbits=serial.STOPBITS_TWO,
		bytesize=serial.SEVENBITS
	)

	ser.isOpen()
	pH=0
	success=0	

	while success==0:
		try : 
			data=map(float, readbuffer(ser).strip().split('\r\n'))
			#print repr(data)
			pH=float(data[0])
			success=1
		except: 
			success= 0 
	return pH




