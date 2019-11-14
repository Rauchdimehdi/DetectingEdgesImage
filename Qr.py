import pyqrcode

def qrcode():
	q=pyqrcode.create('My name is Mehdi Rauchdi')
	q.png('my.png',scale=6)
	print('QR code is generated')

if __name__ == '__main__':
	qrcode()