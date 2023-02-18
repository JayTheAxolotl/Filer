class fileTxt():

	def __init__(self, file):
		self.file = file
	
	def overWrite(self, message):
		myfile = open(self.file, 'w')
		myfile.write(message)
		myfile.close()

	def write(self, message):
		myfile = open(self.file, 'a')
		myfile.write(message)
		myfile.close

	def read(self):
		myfile = open(self.file, 'r')
		message = str(myfile.read())
		return message

	def readEntire(self):
		myfile = open(self.file, 'r')
		message = str(myfile.read())
		return message
	