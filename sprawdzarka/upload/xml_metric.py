import re, mmap
def handle_uploaded_file(f):
	with open('name.txt', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
def xmlmetricf():
	with open('name.txt', 'r+') as f:
		data = mmap.mmap(f.fileno(), 0)
		mo=re.search(r'\<\?xml\sversion=\"1\.0\"\sencoding=\"UTF-8\"\?\>\n*\<\!DOCTYPE\ssprawozdanie\sPUBLIC\s\"sprawozdanie\"\s\"http\:\/\/mhanckow\.vm\.wmi\.amu\.edu\.pl\:20002\/zajecia\/file\-storage\/view\/sprawozdanie\.dtd\"\>\n*\<sprawozdanie\sprzedmiot=\"[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]+\" temat=\"[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]+\"\>\n*<imie_nazwisko\>[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyzźż]+(\s[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyzźż]+)+\<\/imie_nazwisko>\n*<nr_indeksu>[0-9]{6}<\/nr_indeksu>\n*<liczba_pkt>([0-9]|([0-9+\.[0-9]+))<\/liczba_pkt>\n*(<zadanie\snr=\"\-?[0-9]+[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]*\"\spkt=\"([0-9]|([0-9+\.[0-9]+))+\"\>\<\/zadanie>\n*)+\<\/sprawozdanie\>', data)
		if mo:
			print('jes')
			return True
		else:
			print('nie')
			return False
	#		"found error", mo.group(1)

	"""
	s=''
	with open('name.txt', 'r') as f:
		s=f.read()
	if re.search(r'\<\?xml\sversion=\"1\.0\"\sencoding=\"UTF-8\"\?\>\n*\<\!DOCTYPE\ssprawozdanie\sPUBLIC\s\"sprawozdanie\"\s\"http\:\/\/mhanckow\.vm\.wmi\.amu\.edu\.pl\:20002\/zajecia\/file\-storage\/view\/sprawozdanie\.dtd\"\>\n*\<sprawozdanie\sprzedmiot=\"[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]+\" temat=\"[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]+\"\>\n*<imie_nazwisko\>[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyzźż]+(\s[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyzźż]+)+\<\/imie_nazwisko>\n*<nr_indeksu>[0-9]{6}<\/nr_indeksu>\n*<liczba_pkt>([0-9]|([0-9+\.[0-9]+))<\/liczba_pkt>\n*(<zadanie\snr=\"\-?[0-9]+[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]*\"\spkt=\"([0-9]|([0-9+\.[0-9]+))+\"\>\<\/zadanie>\n*)+\<\/sprawozdanie\>',s):
		print('yes')
		return True
	else:
		print('no')
		return False
	"""
	#r'\<\?xml\sversion=\"1\.0\"\sencoding=\"UTF-8\"\?\>\n*\<\!DOCTYPE\ssprawozdanie\sPUBLIC\s\"sprawozdanie\"\s\"http\:\/\/mhanckow\.vm\.wmi\.amu\.edu\.pl\:20002\/zajecia\/file\-storage\/view\/sprawozdanie\.dtd\"\>\n*\<sprawozdanie\sprzedmiot=\"[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]+\" temat=\"[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]+\"\>\n*<imie_nazwisko\>[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyzźż]+(\s[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyzźż]+)+\<\/imie_nazwisko>\n*<nr_indeksu>[0-9]{6}<\/nr_indeksu>\n*<liczba_pkt>([0-9]|([0-9+\.[0-9]+))<\/liczba_pkt>\n*(<zadanie\snr=\"\-?[0-9]+[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]*\"\spkt=\"([0-9]|([0-9+\.[0-9]+))+\"\>\<\/zadanie>\n*)+\<\/sprawozdanie\>', s):

