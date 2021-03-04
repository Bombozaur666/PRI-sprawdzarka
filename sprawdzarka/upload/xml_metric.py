import re, codecs

def handle_uploaded_file(f):
    infile = open(f,'r',encoding = 'utf-8')
    outfile = open('temp.txt','w+', encoding='utf-8')
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()


def xmlmetricf(file):
    # sline = ""
    # for line in file:
    #     sline += str(line.decode("utf-8"))
    # print(sline)

    handle_uploaded_file(file)

    mo = re.compile(r'<\?xml version="1\.0" encoding="UTF-8"\?>\r\n*<!DOCTYPE\ssprawozdanie\sPUBLIC\s"sprawozdanie"\s"http:\/\/mhanckow\.vm\.wmi\.amu\.edu\.pl:20002/zajecia/file-storage/view/sprawozdanie\.dtd">\r\n*<sprawozdanie\sprzedmiot="[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]{3}" temat="[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]{1}">\r\n*<imie_nazwisko>[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyzźż]+(\s[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyzźż]+)+</imie_nazwisko>\r\n*<nr_indeksu>[0-9]{6}</nr_indeksu>\r\n*<liczba_pkt>([0-9]+|([0-9]+\.[0-9]+))</liczba_pkt>\r\n*(<zadanie\snr="-?[0-9]+[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]*"\spkt="([0-9]+|([0-9]+\.[0-9]+))+"></zadanie>\r\n*)+</sprawozdanie>',re.MULTILINE)
    print(mo)

    textfile = open("temp.txt", 'r')
    filetext = textfile.read()
    textfile.close()
    matches = re.findall(mo, filetext)
    print(matches)
    if matches:
        return True
    else:
        return False

    # res = re.findall(mo, sline)
    # print(res)
    # if res:
    #     print('jes')
    #     return True
    # else:
    #     print('nie')
    #     return False
