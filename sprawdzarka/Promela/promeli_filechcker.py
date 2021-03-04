import re, subprocess, os
from .models import TeacherTask, StudentTask, StudentOutput



def promela_funck(snumber):
    List_of_files = StudentTask.objects.filter(has_been_tested=False).all()
    for file in List_of_files:
        ltl = TeacherTask.objects.get(id = file.task_id)
        ss = []
        i = 0
        with open(ltl.file.name) as f:
            ss = f.read().splitlines()
            f.close()
        for x in ss:
            y = re.search(r'^ltl L[0-9]', x)
            if y is not None:
                i += 1
        ltl_amount = i

        file_new = str(file)
        file_new = file_new.replace(".pml", "_result.txt")
        open(file_new, 'w').close()  # czysci plik zeby mozna cat uzyc nizej i nie dodawac w nieskonczonosc tekstu

        file.has_been_tested = True

        subprocess.run(f'spin -a {ltl.file.name} {file.task_file.name}', shell=True)

        out = subprocess.Popen('gcc -o pan pan.c',
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               shell=True)
        stdout, stderr = out.communicate()
        print(stdout)

        if stdout == b'':
            temp = 0
            if ltl_amount == 0:
                command_no_ltl = "./pan -m400000"
                subprocess.run(command_no_ltl, shell=True)
            else:
                for ltl_number in range(ltl_amount):
                    temp += 1
                    command_ltl = f'./pan -a -N L{temp} >> {file_new}'
                    subprocess.run(command_ltl, shell=True)


        object = StudentOutput()
        object.student_task_id = file.id
        object.snumber = snumber
        object.output_file = file_new

        ww = []
        with open(file_new) as f:
            ww = f.read().splitlines()
            f.close()
        for x in ww:
            y = re.search("errors: 0", x)
            if y is not None:
                object.points = ltl.max_points
                break
            else:
                object.points = 0
        object.has_been_graded = True




"""
    List_of_files=Promela.objects.filter(has_been_tested=False).all()
    List_of_ltls=TaskListPromela.objects.all()
    plik_pml = plik_ltl = ""
    ile_razy=0
    for file in List_of_files:
        ile_razy = 0
        ss = []
        do_obliczen = List_of_ltls.filter(id=file.taskid.value)
        with open(file.taskcopy.name) as f:  # tu po kolei kazdy plik do sprawdzenia zadania danego typu
            plik_pml = f.read()
            f.close()
        with open(do_obliczen.ltl_file.name) as f:  # wspolny plik dla wszystkich zadan danego typu
            plik_ltl = f.read()
            ss = f.read().splitlines()
            f.close()
        plik_pml += "\n"
        plik_pml += plik_ltl
        file.update(task=plik_pml)
        for x in ss:
            y = re.search(r'^ltl L[0-9]', x)
            if y is not None:
                ile_razy += 1

#        file_new = file.task.name
#        file_new = file_new.replace(".pml", "_merge.pml")
#        file_new = file_new.replace("task/Promela/Studentstask/", "temp/")
#        with open(file_new, 'w') as fp:  # stworzylem nowe pliki dla testow nie wiem jak to chcesz zrobic docelowo czy tworzyc nowe czy nadpisywac stare
#            fp.write(plik_pml)
#            fp.close()



        file_new = file.taskcopy.name
        open(file_new, 'w').close()  # czysci plik zeby mozna cat uzyc nizej i nie dodawac w nieskonczonosc tekstu
        subprocess.run(f'spin -a {file.taskcopy.name}', shell=True)
        out = subprocess.Popen('gcc -o pan pan.c', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        stdout, stderr = out.communicate()
        if stdout == b'':
            if ile_razy == 0:
                command_no_ltl = "pan -m400000"
                subprocess.run(command_no_ltl, shell=True)
            else:
                for ltl in range(ile_razy):
                    command_ltl = f'pan -a -N L{ltl+1} >> {file_new}'
                    subprocess.run(command_ltl, shell=True)
        lista = []
        dd = []
        with open(file_new) as f:
            dd = f.read().splitlines()
            f.close()
        for x in dd:
            y = re.search("errors: 0", x)
            if y is not None:
                Prom2 = Promela2(taskid=file.taskid.value, snumber=file.snumber.value, task=file.task,output=file.taskcopy,point=TaskListPromela.max_points.filter(taskid=file.taskid), group=file.group.value)
                Prom2.save()
            else:
                Prom2 = Promela2(taskid=file.taskid.value, snumber=file.snumber.value, task=file.task,output=file.taskcopy, group=file.group.value)
                Prom2.save()
                """