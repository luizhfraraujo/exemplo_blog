from zipfile import ZipFile

with ZipFile("meuzip.zip","w") as myzip:
	myzip.write('teste.txt')