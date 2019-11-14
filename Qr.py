import pyqrcode

def qrcode():
	#here you show what you want the scanner to get
	q=pyqrcode.create('My name is Mehdi Rauchdi')
	q.png('my.png',scale=6)
	#just to see this message when the program will be executed
	print('QR code is generated')

if __name__ == '__main__':
	qrcode()