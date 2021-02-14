def get_file(l):
    files_and_enlargement = {}
    for file in l:
        enlargement = ""
        i = len(file) - 1
        while(i >= 0):
            if file[i] == '.':
                enlargement += file[i]
                break
            enlargement += file[i]
            i = i - 1
        enlargement = list(enlargement)
        enlargement.reverse()
        enlargement = "".join([str(i) for i in enlargement])
        if enlargement == '.txt' or enlargement == '.xml':
            files_and_enlargement[file] = enlargement

    return files_and_enlargement

class Report:

    def __init__(self, name_surname, nr_index, count_pkt):
        self.name_surname = name_surname
        self.nr_index = nr_index
        self.count_pkt = count_pkt

    def ReadMetric(self, report):
        i = 0
        name_surname = ""
        nr_index = ""
        count_pkt = ""
        for line in report:
            if i <= 2:
                i = i + 1
                continue
            elif i >= 3 and i <= 5:
                j = 0
                was = False
                while line != "" and j < len(line):
                    if was == True:
                        break
                    if line[j] == '>':
                        j = j + 1
                        if line[j] == '<':
                            if i == 3:
                                name_surname += '-'
                            elif i == 4:
                                nr_index += '-'
                            elif i == 5:
                                count_pkt += '-'
                            break
                        was = True
                        while True:
                            if i == 3:
                                name_surname += line[j]
                            elif i == 4:
                                nr_index += line[j]
                            elif i == 5:
                                count_pkt += line[j]
                            j = j + 1
                            if line[j] == '<':
                                break
                    else:
                        j = j + 1
            elif i > 5:
                break
            i = i + 1
        return name_surname, nr_index, count_pkt

class ProgramFile(Report):

    def get_words(self, file1, file2):
        temp1 = [[word for word in line.split(' ')] for line in file1]
        words1 = []
        for list1 in temp1:
            if list1[0] == '\n' or list1[0] == 'Zadanie':
                continue
            words1.extend(list1)
        clear_words1 = []
        chars = ['?', '!', ':', ';', '.', '(', ')', '\n', ',', '\t', '?\n', '!\n', '.\n', ',\n', ':\n', ';\n', '(\n', ')\n']
        for word in words1:
            #words1.remove(word)
            word = list(word)
            for i in range(len(word)):
                if word[i] in chars:
                    word[i] = ""
            clearword1 = "".join(word)
            clear_words1.append(clearword1)

        temp2 = [[word for word in line.split(' ')] for line in file2]
        words2 = []
        for list2 in temp2:
            if list2[0] == '\n' or list2[0] == 'Zadanie':
                continue
            words2.extend(list2)
        clear_words2 = []
        chars = ['?', '!', ':', ';', '.', '(', ')', '\n', ',', '\t', '?\n', '!\n', '.\n', ',\n', ':\n', ';\n', '(\n', ')\n']
        for word in words2:
            #words2.remove(word)
            word = list(word)
            for i in range(len(word)):
                if word[i] in chars:
                    word[i] = ""
            clearword2 = "".join(word)
            clear_words2.append(clearword2)
        return clear_words1, clear_words2

    def get_textlist(self, list_of_file1, list_of_file2):
        text_list1 = []
        text_list2 = []
        appeared1 = False
        appeared2 = False
        for word1 in list_of_file1:
            if word1 == '</sprawozdanie>':
                appeared1 = True
                continue
            if appeared1 == True and word1 != '':
                text_list1.append(word1)

        for word2 in list_of_file2:
            if word2 == '</sprawozdanie>':
                appeared2 = True
                continue
            if appeared2 == True and word2 != '':
                text_list2.append(word2)
        del(list_of_file1)
        del(list_of_file2)

        return text_list1, text_list2

    def remove_repeat(self, text1, text2):
        not_repeat1 = []
        not_repeat2 = []
        for word1 in text1:
            if word1 not in not_repeat1:
                not_repeat1.append(word1)
            else:
                continue
        for word2 in text2:
            if word2 not in not_repeat2:
                not_repeat2.append(word2)
            else:
                continue
        return not_repeat1, not_repeat2

    def check_words(self, words_list1, words_list2):
        if len(words_list1) >= len(words_list2):
            the_same = []
            words_to_check = []
            for w in words_list2:
                checked = w
                if checked in words_list1:
                    the_same.append(checked)
                else:
                    i = 0
                    while i < len(words_list1):
                        if abs(len(checked) - len(words_list1[i])) > 0 and abs(len(checked) - len(words_list1[i])) <= 3:
                            words_to_check.append(checked)
                            break
                        else:
                            i = i + 1
        else:
            the_same = []
            words_to_check = []
            for w in words_list1:
                checked = w
                if checked in words_list2:
                    the_same.append(checked)
                else:
                    j = 0
                    while j < len(words_list2):
                        if abs(len(checked) - len(words_list2[j])) > 0 and abs(len(checked) - len(words_list2[j])) <= 3:
                            words_to_check.append(checked)
                            break
                        else:
                            j = j + 1
        count_of_the_same = len(the_same)
        #print(words_list1)
        #print(words_list2)
        return words_to_check, count_of_the_same

    def check_the_similar_words(self, checked, list_of_words):
        positive = 0
        if checked.isdigit() == False: #nie porównuj podobieństwa liczb pomiędzy sobą
            for word in list_of_words:
                if word.isdigit() == True:
                    continue
                if len(checked) <= len(word):
                    length = len(checked)
                elif len(checked) > len(word):
                    length = len(word)
                i = 0
                negative = 0
                first = False
                is_already_negative = False
                this_is_not_similar = False
                while i < length:
                    if i == 0 and checked[0].lower() == word[0].lower():
                        first = True
                        i = i + 1
                        continue
                    if checked[i] == word[i] and negative <= 3:
                        if not is_already_negative == True:
                            i = i + 1
                        else:
                            this_is_not_similar = True
                            break
                    elif checked[i] == word[i] and negative > 3:
                        this_is_not_similar = True
                        break
                    elif checked[i] != word[i] and negative <= 3:
                        is_already_negative = True
                        negative += 1
                        i = i + 1
                    elif checked[i] != word[i] and negative > 3:
                        this_is_not_similar = True
                        negative += 1
                        break
                negative += abs(len(checked) - len(word))
                if negative <= 3 and first == True and this_is_not_similar == False:
                    positive = positive + 1
            return positive
        else:
            return positive

    # pat -> wzór
    # txt -> text
    # q -> liczba pierwsza
    def Rabin_Karp_algorithm(self, pat, txt, q):
        if (type(pat) is str) and (type(txt) is str) and (type(q) is int):
            M = len(pat)
            N = len(txt)
            i = 0
            j = 0
            p = 0  # wartość hasha dla wzoru
            t = 0  # wartość hasha dla tekstu
            h = 1
            d = 256
            similars = []

            # Wartość h powinna mieć wartość 'pow(d, M-1) % q'
            for i in range(M - 1):
                h = (h * d) % q

            # Przelicz wartość hasha wzoru i hasha pierwszego podciągu tekstu
            for i in range(M):
                p = (d * p + ord(pat[i])) % q
                t = (d * t + ord(txt[i])) % q

            # Przeglądaj wzór w tekście jeden po drugim
            for i in range(N - M + 1):  # Sprawdź wartości hash dla obecnego tekstu i wzoru
                if p == t:  # jeśli wartość hasha pasuje wtedy tylko sprawdź dla każdego znaku z osobna
                    for j in range(M):  # Sprawdź znak po znaku
                        if txt[i + j] != pat[j]:
                            break
                    j += 1
                    if j == M:
                        similars.append(i)
                        #print(pat)
                        #print("Pattern found at index " + str(i))

                if i < N - M:  # Przelicz wartość hasha dla kolejnego tekstu
                    t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
                    if t < 0:  # Możemy mieć wartość ujemną t. Konwertujemy na dodatnią
                        t = t + q
            return similars

        else:
            raise Exception("Co najmniej jeden parametr jest niepoprawny")

if __name__ == '__main__':
    already_checked_files = []
    files_and_enlargement = get_file()
    for first_file in files_and_enlargement:
        already_checked_files.append(first_file)
        for second_file in files_and_enlargement:
            if first_file != second_file and second_file not in already_checked_files:
                print()
                print("Sprawdzam ", first_file, " i ", second_file)
                if (files_and_enlargement[first_file] == ".txt" and files_and_enlargement[second_file] == '.txt') or (files_and_enlargement[first_file] == ".txt" and files_and_enlargement[second_file] == ".xml") or (files_and_enlargement[first_file] == ".xml" and files_and_enlargement[second_file] == ".txt") or (files_and_enlargement[first_file] == ".xml" and files_and_enlargement[second_file] == ".xml"):
                    file1 = open(first_file, 'r', encoding="utf-8", errors="ignore")
                    file2 = open(second_file, 'r', encoding="utf-8", errors="ignore")
                    report = ProgramFile("Bartlomiej Nowak", "434589", "15")
                    name_surname1, nr_index1, count_pkt1 = report.ReadMetric(file1)
                    name_surname2, nr_index2, count_pkt2 = report.ReadMetric(file2)
                    words1, words2 = report.get_words(file1, file2)
                    text1, text2 = report.get_textlist(words1, words2)
                    not_repeat1, not_repeat2 = report.remove_repeat(text1, text2)
                    similars = []
                    txt = ""
                    q = 101  # Liczba pierwsza
                    if len(not_repeat1) > 0 and len(not_repeat2) > 0:
                        if len(not_repeat1) >= len(not_repeat2):
                            txt = " ".join([str(i) for i in not_repeat1])
                            for word in not_repeat2:
                                indexes = []
                                indexes = report.Rabin_Karp_algorithm(word, txt, q)
                                if len(indexes) > 0:
                                    if word not in similars:
                                        similars.append(word)
                                    else:
                                        continue
                            total = len(not_repeat1)
                            count_of_the_same_or_similar = len(similars)
                            plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
                        else:
                            txt = " ".join([str(i) for i in not_repeat2])
                            for word in not_repeat1:
                                indexes = []
                                indexes = report.Rabin_Karp_algorithm(word, txt, q)
                                if len(indexes) > 0:
                                    if word not in similars:
                                        similars.append(word)
                                    else:
                                        continue
                            total = len(not_repeat2)
                            count_of_the_same_or_similar = len(similars)
                            plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
                        if plagiarism_coefficient >= 30 and plagiarism_coefficient <= 100:
                            print(plagiarism_coefficient, "% podobieństwa")
                            print("PLAGIAT!!!")
                            if (name_surname1 == '-' or nr_index1 == '-' or count_pkt1 == '-') and (name_surname2 == '-' or nr_index2 == '-' or count_pkt2 == '-'):
                                print("Nie można zweryfikować wszystkich danych obu studentów w plikach ", first_file, " i ", second_file)
                            elif name_surname1 == '-' or nr_index1 == '-' or count_pkt1 == '-':
                                print("Nie można zweryfikować wszystkich danych studenta w pliku ", first_file)
                                print("Osoba, która dopuściła się plagiatu to:")
                                print(name_surname2, " o numerze indeksu ", nr_index2)
                            elif name_surname2 == '-' or nr_index2 == '-' or count_pkt2 == '-':
                                print("Osoba, która dopuściła się plagiatu to:")
                                print(name_surname1, " o numerze indeksu ", nr_index1)
                                print("Nie można zweryfikować wszystkich danych studenta dla pliku ", second_file)
                            else:
                                print("Osoby które dopuściły się plagiatu to:")
                                print(name_surname1, " o numerze indeksu ", nr_index1)
                                print(name_surname2, " o numerze indeksu ", nr_index2)
                        else:
                            print(plagiarism_coefficient, "% podobieństwa")
                            print("NIE MA PLAGIATU!!")
                    else:
                        print("Nie można sprawdzić plagiatu dla plików pustych lub bez rozwiązania")
                else:
                    continue
            else:
                continue

