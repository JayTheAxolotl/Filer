from filer import fileTxt

HelloText = fileTxt("Hello.txt")

print(HelloText.read()[0])