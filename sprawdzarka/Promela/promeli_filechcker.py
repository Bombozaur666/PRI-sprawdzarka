import re, subprocess, os
from .models import TeacherTask, StudentTask

def promela_funck():
    List_of_files = StudentTask.objects.filter(has_been_tested=False).all()
    for file in List_of_files:
        ltl = TeacherTask.objects.get(id = file.task_id.id)
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

        file_new = str(file.task_file.name)
        file.output_file.name=file_new.replace(".pml", "_result.txt") 
        file_new = file_new.replace(".pml", "_result.txt")
        open(file_new, 'w').close()

        file.has_been_tested = True
        ltl_cos_1="C:\\PRI-sprawdzarka\\sprawdzarka\\"
        ltl_cos_1+=ltl.file.name.replace('/','\\')

        ltl_cos_2="C:\\PRI-sprawdzarka\\sprawdzarka\\"
        ltl_cos_2+=file.task_file.name.replace('/','\\')
        print(ltl_cos_1)
        print(ltl_cos_2)
        subprocess.run(f'spin -a -N {ltl_cos_1} {ltl_cos_2}', shell=True)
        print('po spin--------------------------------------------')
        out = subprocess.Popen('gcc -o pan pan.c',
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               shell=True)
        stdout, stderr = out.communicate()
        print('po gcc--------------------------------------------')
        if stdout == b'':
            temp = 0
            if ltl_amount == 0:
                command_no_ltl = "C:\\PRI-sprawdzarka\\sprawdzarka\\pan -m400000"
                subprocess.run(command_no_ltl, shell=True)
            else:
                for ltl_number in range(ltl_amount):
                    temp += 1
                    command_ltl = f'C:\\PRI-sprawdzarka\\sprawdzarka\\pan -a -N L{temp} >> {file_new}'
                    subprocess.run(command_ltl, shell=True)
                    print('else--------------------------------------------')
        ww = []
        with open(file_new) as f:
            ww = f.read().splitlines()
            f.close()
        for x in ww:
            y = re.search("errors: 0", x)
            if y is not None:
                file.points=ltl.max_points
                break
            else:
                file.points = -1
        file.has_been_tested=True
        file.save()