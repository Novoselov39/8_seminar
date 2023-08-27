def dell_contact(phonebook, last_name):    
    result=[]
    
    for contact in phonebook:
        if (contact['last_name'].lower()==last_name.lower()):
            result.append(contact)
            
    if len(result) >1:
        print(f"Найдено {len(result)} контактов с данной фамилией:")
        veiews_contacts(result)
        index = int(input("Введите номер контакта, который хотите удалить: "))
        result = [result[index-1]]
     
    
    if result:
        phonebook.remove(result[0])
        return True
    else:
        return False


def change_contact(phonebook, last_name):
    result=[]
    
    for contact in phonebook:
        if (contact['last_name'].lower()==last_name.lower()):
            result.append(contact)
            
    if len(result) >1:
        print(f"Найдено {len(result)} контактов с данной фамилией:")
        veiews_contacts(result)
        index = int(input("Введите номер контакта, который хотите изменить: "))
        result = [result[index-1]]
    
    if result:
        for contact in phonebook:
            if contact == result[0]:
                contact['last_name']=input("Введи новую фамилию: ")
                contact['first_name']=input("Введи новое имя: ")
                contact['middle_name']=input("Введи новое отчество: ")
                contact['phone_number']=input("Введи новый телефон: ")
                
                break
    
        return True
    else:
        return False
        

def load_file(filename):
    phonebook=[]
    try:
        with open(filename, 'r') as file:
            for contact in file:
                last_name, first_name, middle_name, phone_number=contact.split(",")
                phonebook.append({
                    'last_name':last_name,
                    'first_name':first_name,
                    'middle_name':middle_name,
                    'phone_number':phone_number.replace("\n","")
                })
    except FileNotFoundError:
        print("файл не найден")       
    return phonebook


def search_contacts(phonebook, search_key):
    result=[]
    for contact in phonebook:
        if (search_key.lower() in contact['last_name'].lower()) or (search_key.lower() in contact['first_name'].lower()):
            result.append(contact)
    return result
            


def veiews_contacts(phonebook):
    print("---------------------")
    for index, contact in enumerate(phonebook, start=1):
        print(f"{index}, {contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}")
    print("---------------------")


def save_to_file(filename, phonebook):
    with open(filename,'w') as file:
        for  contact in phonebook:
            file.write(f"{contact['last_name']},{contact['first_name']},{contact['middle_name']},{contact['phone_number']} \n")


def add_contact(phonebook, last_name, first_name, middle_name, phone_number):
    contact={
        'last_name':last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    }
    phonebook.append(contact)
    print("Контакт добавлен")


def main():
    phonebook=[
        {'last_name':"иванов",
         'first_name': "петр",
        'middle_name': "Иванович",
        'phone_number': "67890"},
          {'last_name':"Новоселов",
         'first_name': "анатолий",
        'middle_name': "Иванович",
        'phone_number': "67890"},
          {'last_name':"петров",
         'first_name': "толя",
        'middle_name': "Иванович",
        'phone_number': "67890"},
        {'last_name':"Иванов",
         'first_name': "толя",
        'middle_name': "Иванович",
        'phone_number': "67890"},
    ]
    filename="phonebook.txt"    
    while True:

        print("1. добавить контакт")
        print("2. сохранить в файл")
        print("3. вывести все контакты")
        print("4. поиск по имени/фафмилии")
        print("5. загрузить из файла")
        print("6. Изменить контакт")
        print("7. удалить контакт")
        print("8. выйти")

        choise=input("Выберите действие: ")

        if choise=='1':
            last_name=input("Фамилия: ")
            first_name=input("Имя: ")
            middel_name=input("Отчество: ")
            phone_number=input("Телефон: ")
            add_contact(phonebook, last_name, first_name, middel_name, phone_number)
        elif choise=="2":
            save_to_file(filename, phonebook)
        elif choise=="3":
            veiews_contacts(phonebook)
        elif choise=="4":
            search_key=input("Введи запрос: ")
            result=search_contacts(phonebook,search_key)
            if result:
                print("Найден следующие контакты:")                
                veiews_contacts(result)
            else:
                print("Контакты не найдены!")
        elif choise=="5":
            print()
            phonebook=load_file(filename)
            veiews_contacts(phonebook)
            print()
        elif choise=="6":
            last_name = input("Введи фаимилию изменяемого контакта: ")            
            if change_contact(phonebook, last_name):
                print("Контакт изменен")
            else:
                print("Контакт не найден")
        elif choise=="7":
            last_name = input("Введи фаимилию удаляемого контакта: ")            
            if dell_contact(phonebook, last_name):
                print("Контакт удален")
            else:
                print("Контакт не найден")
        elif choise=="8":
            break
    
       
        
        
    



if __name__=="__main__":
    main()