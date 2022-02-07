import csv

users_data = []


def writer(filename, header, data):
    with open(filename, "w", newline="", encoding="utf8") as csvfile:
        all = csv.writer(csvfile)
        all.writerow(header)
        for x in data:
            all.writerow(x)


def ready_up(info):
    with open(info, encoding="utf8")as f:
        users_data = csv.DictReader(f, delimiter=",")
        temp = []
        for row in users_data:
            row['esm'] = row['esm'].replace(" ", "")
            row['famil'] = row['famil'].replace(" ", "")
            row['keshvar'] = row['keshvar'].replace(" ", "")
            row['rang'] = row['rang'].replace(" ", "")
            row['ashia'] = row['ashia'].replace(" ", "")
            row['ghaza'] = row['ghaza'].replace(" ", "")
            temp.append((row['esm'], row['famil'], row['keshvar'], row['rang'], row['ashia'], row['ghaza']))
        return temp


def add_participant(participant, **answers):
    users_data.append((participant.replace(" ", ""), answers['esm'].replace(" ", ""), answers['famil'].replace(" ", ""),
                       answers['keshvar'].replace(" ", ""), answers['rang'].replace(" ", ""),
                       answers['ashia'].replace(" ", ""),
                       answers['ghaza'].replace(" ", "")))


def calculate_all():
    result = {}
    esm, famil, keshvar, rang, ashia, ghaza = [], [], [], [], [], []
    with open("game_data.csv", encoding="utf8") as f:
        user_dic = csv.DictReader(f, delimiter=",")
        for user in user_dic:
            if user['esm'] == '':
                esm.append(user['participant'])
            if user['famil'] == '':
                famil.append(user['participant'])
            if user['keshvar'] == '':
                keshvar.append(user['participant'])
            if user['rang'] == '':
                rang.append(user['participant'])
            if user['ashia'] == '':
                ashia.append(user['participant'])
            if user['ghaza'] == '':
                famil.append(user['participant'])

        print(esm, famil, keshvar, rang, ashia, ghaza)
        esm_repeat, famil_repeat, keshvar_repeat, rang_repeat, ashia_repeat, ghaza_repeat = [], [], [], [], [], []
    with open("game_data.csv", encoding="utf8") as f:
        user_dic = csv.DictReader(f, delimiter=",")
        for user in user_dic:
            with open("game_data.csv", encoding="utf8") as f:
                user_dic = csv.DictReader(f, delimiter=",")
                for user1 in user_dic:
                    if user1['participant'] != user['participant']:
                        if user['esm'] == user1['esm']:
                            esm_repeat.append(user['participant'])
                        if user['famil'] == user1['famil']:
                            famil_repeat.append(user['participant'])
                        if user['keshvar'] == user1['keshvar']:
                            keshvar_repeat.append(user['participant'])
                        if user['rang'] == user1['rang']:
                            rang_repeat.append(user['participant'])
                        if user['ashia'] == user1['ashia']:
                            ashia_repeat.append(user['participant'])
                        if user['ghaza'] == user1['ghaza']:
                            ghaza_repeat.append(user['participant'])
        print(esm_repeat, famil_repeat, keshvar_repeat, rang_repeat, ashia_repeat, ghaza_repeat)
    with open("game_data.csv", encoding="utf8") as f:
        user_dic = csv.DictReader(f, delimiter=",")
        for user in user_dic:
            counter = 0
            with open("esm_famil_data_1.csv", encoding="utf8") as f:
                users_data = csv.DictReader(f, delimiter=",")
                if len(esm) != 0:
                    for row in users_data:
                        if row['esm'] == user['esm'] and row['esm'] != '' and user['esm'] != '':
                            if user['participant'] not in esm_repeat:
                                counter += 15
                            else:
                                counter += 10
                else:
                    for row in users_data:
                        if row['esm'] == user['esm'] and row['esm'] != '':
                            if user['participant'] not in esm_repeat:
                                counter += 10
                            else:
                                counter += 5
            #############################
            with open("esm_famil_data_1.csv", encoding="utf8") as f:
                users_data = csv.DictReader(f, delimiter=",")
                if len(famil) != 0:
                    for row in users_data:
                        if row['famil'] == user['famil'] and row['famil'] != '' and user['famil'] != '':
                            if user['participant'] not in famil_repeat:
                                counter += 15
                            else:
                                counter += 10
                else:
                    for row in users_data:
                        if row['famil'] == user['famil'] and row['famil'] != '':
                            if user['participant'] not in famil_repeat:
                                counter += 10
                            else:
                                counter += 5
            ##############################
            with open("esm_famil_data_1.csv", encoding="utf8") as f:
                users_data = csv.DictReader(f, delimiter=",")
                if len(keshvar) != 0:
                    for row in users_data:
                        if row['keshvar'] == user['keshvar'] and row['keshvar'] != '' and user['keshvar'] != '':
                            if user['participant'] not in keshvar_repeat:
                                counter += 15
                            else:
                                counter += 10
                else:
                    for row in users_data:
                        if row['keshvar'] == user['keshvar'] and row['keshvar'] != '':
                            if user['participant'] not in keshvar_repeat:
                                counter += 10
                            else:
                                counter += 5
            ##############################
            with open("esm_famil_data_1.csv", encoding="utf8") as f:
                users_data = csv.DictReader(f, delimiter=",")
                if len(rang) != 0:
                    for row in users_data:
                        if row['rang'] == user['rang'] and row['rang'] != '' and user['rang'] != '':
                            if user['participant'] not in rang_repeat:
                                counter += 15
                            else:
                                counter += 10
                else:
                    for row in users_data:
                        if row['rang'] == user['rang'] and row['rang'] != '':
                            if user['participant'] not in rang_repeat:
                                counter += 10
                            else:
                                counter += 5
            ##############################
            with open("esm_famil_data_1.csv", encoding="utf8") as f:
                users_data = csv.DictReader(f, delimiter=",")
                if len(ashia) != 0:
                    for row in users_data:
                        if row['ashia'] == user['ashia'] and row['ashia'] != '' and user['ashia'] != '':
                            if user['participant'] not in ashia_repeat:
                                counter += 15
                            else:
                                counter += 10
                else:
                    for row in users_data:
                        if row['ashia'] == user['ashia'] and row['ashia'] != '':
                            if user['participant'] not in ashia_repeat:
                                counter += 10
                            else:
                                counter += 5
            ##############################
            with open("esm_famil_data_1.csv", encoding="utf8") as f:
                users_data = csv.DictReader(f, delimiter=",")
                if len(ghaza) != 0:
                    for row in users_data:
                        if row['ghaza'] == user['ghaza'] and row['ghaza'] != '' and user['ghaza'] != '':
                            if user['participant'] not in ghaza_repeat:
                                counter += 15
                            else:
                                counter += 10
                else:
                    for row in users_data:
                        if row['ghaza'] == user['ghaza'] and row['ghaza'] != '':
                            if user['participant'] not in ghaza_repeat:
                                counter += 10
                            else:
                                counter += 5
                ##############################

                result.update({user['participant']: counter})
    return result


def start():
    all_data=ready_up("esm_famil_data.csv")
    filename = 'esm_famil_data_1.csv'
    header = ('esm', 'famil', 'keshvar', 'rang', 'ashia', 'ghaza')
    writer(filename, header, all_data)
    while True:
        user_input = input("Do you continue (yes/no)?")
        answers = {}
        if user_input == 'yes':
            participant = input("participant:")
            answers['esm'] = input("Enter esm:")
            answers['famil'] = input("Enter famil:")
            answers['keshvar'] = input("Enter keshvar:")
            answers['rang'] = input("Enter rang:")
            answers['ashia'] = input("Enter ashia:")
            answers['ghaza'] = input("Enter ghaza:")
            add_participant(participant, **answers)
            continue
        else:
            filename = "game_data.csv"
            header = ('participant', 'esm', 'famil', 'keshvar', 'rang', 'ashia', 'ghaza')
            writer(filename,header,users_data)
            result = calculate_all()
            print(result)
            break


if __name__ == '__main__':
    start()
