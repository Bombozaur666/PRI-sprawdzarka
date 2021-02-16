import os, re, subprocess

#STEP 1 - get all the files (later from a database i guess)

location = os.getcwd() #current dir, later change to specified location

#STEP 2 - merge plikow pml i ltl

plik_pml = plik_ltl = ""

for file in os.listdir(location):
	if file.endswith(".pml") and not file.endswith("_merge.pml"):
		with open(file) as f: #tu po kolei kazdy plik do sprawdzenia zadania danego typu
			plik_pml = f.read()
			
		with open("np02b_ltl.txt") as f: #wspolny plik dla wszystkich zadan danego typu
			plik_ltl = f.read()
			
		plik_pml += "\n"
		plik_pml += plik_ltl
		
		file_new = str(file)
		file_new = file_new.replace(".pml", "_merge.pml")

		with open (file_new, 'w') as fp: #stworzylem nowe pliki dla testow nie wiem jak to chcesz zrobic docelowo czy tworzyc nowe czy nadpisywac stare
			fp.write(plik_pml)
	
#kod od bombo uzywam do sprawdzenia ile jest LTLow	

ltl_lista = []
ss = []
with open("np02b_ltl.txt") as f:
	ss=f.read().splitlines()
	f.close()
for x in ss:
	y = re.search(r'^ltl L[0-9]', x)
	if y is not None:
		ltl_lista.append(file)
ltl_amount = len(ltl_lista)
	
#STEP 3 - skompilowanie plikow w promeli, zapisanie wydrukow

for file in os.listdir(location):
	if file.endswith("_merge.pml"):
	
		file_new = str(file)
		file_new = file_new.replace("_merge.pml", "_result.txt")
		open(file_new, 'w').close() #czysci plik zeby mozna cat uzyc nizej i nie dodawac w nieskonczonosc tekstu

		subprocess.run(f'spin -a {file}', shell=True)
		
		out = subprocess.Popen('gcc -o pan pan.c', 
			stdout=subprocess.PIPE, 
			stderr=subprocess.STDOUT,
			shell=True)
		stdout,stderr = out.communicate()
		print(stdout)
		
		if stdout == b'':
			temp = 0
			if not ltl_lista:
				command_no_ltl = "./pan -m400000"
				subprocess.run(command_no_ltl, shell=True)
			else:
				for ltl in ltl_lista:
					temp += 1
					command_ltl = f'./pan -a -N L{temp} >> {file_new}'
					print(command_ltl)
					subprocess.run(command_ltl, shell=True)
		
	

#ponizej jest kod od bombo ktory otwiera pliki z wynikami i sprawdza czy error 0 byl

lista = []
ss = []
for file in os.listdir(location):
	if file.endswith("_result.txt"):
		with open(file) as f:
			ss=f.read().splitlines()
			f.close()
		for x in ss:
			y = re.search("errors: 0", x)
			if y is not None:
				lista.append(file)
print(lista)#to takie for now zeby cos zwracalo
	

