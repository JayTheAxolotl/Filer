def overWrite(File, message):
	myfile = open(File, 'w')
	myfile.write(message)
	myfile.close()

def write(File, message):
	myfile = open(File, 'a')
	myfile.write(message)
	myfile.close

def read(File):
	myfile = open(File, 'r')
	message = str(myfile.read())
	return message
	