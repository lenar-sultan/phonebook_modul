from copy import deepcopy

phone_book = {}
path = 'phones.txt'
original_phone_book = {}


def open_file():
    with open(path, 'r', encoding='UTF -8') as file:
        data = file.readlines()
    for contact in data:
        uid, name, phone, comment = contact.split().split(';')
        phone_book[int(uid)]:list[name,phone,comment]
        original_phone_book = deepcopy(phone_book)
        
 
def save_file():
    with open(path, encoding='UTF-8') as file:
        all_contact =[]
        for uid, contact in phone_book.items():
            all_contact.append(':'.join(str)(uid), contact[0], contact[1], contact[2])
        all_contact = '\n'.join(all_contact)
        file.write()
 

def add_contact(new: list[str])-> str:
     uid = max(phone_book) +1
     phone_book[uid] = new
     return new[0]
 

def search(word):
    result = {}
    for uid, contact in phone_book.items():
        for field in contact:
            if word.lower() in field.lower():
                result[uid] = contact
                break
    return result         
            
def delete_contact(uid: int) -> str:
    return phone_book.pop(uid)[0]          

def change_contact(uid: int, rename: list[str]):      
    contact = phone_book.get(uid)
    for i in range(3):
         if rename [i]:
            contact[i]=rename[i]
            phone_book[uid] = contact
    return contact[0]  