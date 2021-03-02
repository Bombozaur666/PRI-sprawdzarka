import re, mmap
def handle_uploaded_file(f):
	with open('name.txt', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
def xmlmetricf(file):
	sline=""
	for line in file:
		sline+=str(line.decode("utf-8") )
	print(sline)

	mo=re.compile(r'\<\?xml\sversion=\"1\.0\"\sencoding=\"UTF-8\"\?\>\n*\<\!DOCTYPE\ssprawozdanie\sPUBLIC\s\"sprawozdanie\"\s\"http\:\/\/mhanckow\.vm\.wmi\.amu\.edu\.pl\:20002\/zajecia\/file\-storage\/view\/sprawozdanie\.dtd\"\>\n*\<sprawozdanie\sprzedmiot=\"[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]+\" temat=\"[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]+\"\>\n*<imie_nazwisko\>[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyzźż]+(\s[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyzźż]+)+\<\/imie_nazwisko>\n*<nr_indeksu>[0-9]{6}<\/nr_indeksu>\n*<liczba_pkt>([0-9]|([0-9+\.[0-9]+))<\/liczba_pkt>\n*(<zadanie\snr=\"\-?[0-9]+[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]*\"\spkt=\"([0-9]|([0-9+\.[0-9]+))+\"\>\<\/zadanie>\n*)+\<\/sprawozdanie\>',re.MULTILINE)
	res=mo.match(sline)
	if res:
		print('jes')
		return True
	else:
		print('nie')
		return False