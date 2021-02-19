import os, re, subprocess
from .models import Promela, TaskListPromela
# STEP 1 - get all the files (later from a database i guess)


def promela():
    List_of_files=Promela.objects.filter(has_been_tested=False).all()
    List_of_ltls=TaskListPromela.objects.all()
    plik_pml = plik_ltl = ""

    for file in List_of_files:
        ile_razy=0
        ltl_lista = []
        ss = []
        do_obliczen = List_of_ltls.filter(id=file.taskid.value)

        with open(file.task.name) as f:  # tu po kolei kazdy plik do sprawdzenia zadania danego typu
            plik_pml = f.read()
            f.close()
        with open(do_obliczen.ltl_file.name) as f:  # wspolny plik dla wszystkich zadan danego typu
            plik_ltl = f.read()
            f.close()

        with open(do_obliczen.ltl_file.name) as f:
            ss = f.read().splitlines()
            f.close()

        for x in ss:
            y = re.search(r'^ltl L[0-9]', x)
            if y is not None:
                ltl_lista.append(file)
        ile_razy = len(ltl_lista)
        plik_pml += "\n"
        plik_pml += plik_ltl

        file_new = file.task.name
        file_new = file_new.replace(".pml", "_merge.pml")

        with open(file_new, 'w') as fp:  # stworzylem nowe pliki dla testow nie wiem jak to chcesz zrobic docelowo czy tworzyc nowe czy nadpisywac stare
            fp.write(plik_pml)
            fp.close()

        if file.endswith("_merge.pml"):
            file_new = str(file)
            file_new = file_new.replace("_merge.pml", "_result.txt")
            open(file_new, 'w').close()  # czysci plik zeby mozna cat uzyc nizej i nie dodawac w nieskonczonosc tekstu
            subprocess.run(f'spin -a {file}', shell=True)
            out = subprocess.Popen('gcc -o pan pan.c',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            stdout, stderr = out.communicate()
            if stdout == b'':
                temp = 0
                if not ltl_lista:
                    command_no_ltl = "./pan -m400000"
                    subprocess.run(command_no_ltl, shell=True)
                else:
                    for ltl in ltl_lista:
                        temp += 1
                        command_ltl = f'./pan -a -N L{temp} >> {file_new}'
                        subprocess.run(command_ltl, shell=True)
        lista = []
        lines = []
        #tu bedzie zabawa xd
"""
        if file.endswith("_result.txt"):
            with open(file) as f:
                lines = f.read().splitlines()
                f.close()
            for x in lines:
                y = re.search("errors: 0", x)
                if y is not None:
                    lista.append(file)
"""