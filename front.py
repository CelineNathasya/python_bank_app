from os import system
import json
import datetime
from model.user import User, load_users, add_user, remove_user, edit_user, block_user, edit_balance

def load_user():
    with open('User.json') as f:
        data = json.load(f)
    return data

def to_json_by_Cy(data):
    with open('User.json','w') as f :
        json.dump(data, f, indent=4)

def login():
    users = load_users()
    while True:
        userid = False
        login_fail = 4
        system('cls')
        print("{:=^50}".format('Welcome To Bank ITU'))
        print("{:=^50}".format('Login'))

        user_id = input("ID    : ")
        user_pin = input("PIN   : ")
        
        for user in users:
            if user_id == user.id:
                userid = True
                while login_fail!=0:
                    if user_pin == user.pin:
                        if user.status == "inactive":
                            print('Your account is blocked, contact your admin')
                            system("pause")
                            break
                        else:
                            print('Login berhasil')
                            return user
                    else:
                        system('cls')
                        print("{:=^50}".format('Login'))
                        print('Try again, Kesempatan',login_fail)
                        print('ID    :',user_id)
                        user_pin = input("PIN   : ")
                        if user_pin == user.pin:
                            if user.status == "inactive":
                                print('Your account is blocked, contact your admin')
                                system("pause")
                                break
                            else:
                                print('Login berhasil')
                                return user
                        else:
                            login_fail -= 1
                            
                    if login_fail == 0:
                        print('Your Account has been blocked')
                        print('contact admin!!')
                        system('pause')
                        block_user(user_id)
                        break
                        

                    print('PIN salah')
                    try_again_choice = ['yes',"y","no",'n']    
                    try_again = input('Continue (y/n) ? ')
                    while try_again not in try_again_choice: 
                        try_again = input('Continue (y/n) ? ')
                    if try_again == "n":
                        break

        if userid == False:    
            print('ID or PIN Wrong !!')
            system('pause')


def cek_saldo(data):
    all_user = load_users()
    for user in all_user:
        if user.id == data.id:
            print(f'\n\nYour Balance : Rp. {user.balance:,.2f}')

# di abadikan
# def setor(setoran,data):
#     all_data = load_user()
#     list_data = []
#     for user in all_data:
#         if user['name'] == data['name']:
#             edit_balance(user)
#             print(f'anda telah melakukan transaksi sebesar Rp. {setoran:,.2f}')
#         list_data.append(user)
#     system('pause')          
#     return to_json_by_Cy(list_data)   
    

# def tarik(quantity,data):
#     all_data = load_user()
#     list_data = []
#     pin = False
#     if quantity > data['balance']:
#         print('Saldo anda tidak cukup')
#     else :
#         for user in all_data:  
#             if user['id'] == data['id']:
#                 user['balance'] = data['balance'] - quantity
#                 print(f'Jumlah yang ingin anda tarik {quantity:,.2f}')
#                 print('Masukan PIN untuk melanjutkan')
#                 user_input = input('PIN : ')
#                 if user_input == data['pin']:
#                     pin = True
#                     print('sukses')
#                 else:
#                     print('PIN anda salah')  
#             list_data.append(user)
#     system('pause')
#     if pin == True:
#         return to_json_by_Cy(list_data)

def transfer(data):
    all_data = load_user()
    list_data = []
    print('======Transfer======')

    target_transfer = input('ID penerima : ')
    target = False

    if data['id'] == target_transfer:   #jika id sender dan receiver sama
        print("Anda tidak bisa melakukan Transfer ke Rekening sendiri")
        system('pause')
        return False

    for x in all_data:
        if target_transfer == x['id']:
            target = True
    if target == False:
        print('ID Tidak ditemukan')
        system('pause')
        return False

    for user in all_data:
        if user['id'] == data['id']:
            
            nominal = int(input('Jumlah : Rp. '))
            if nominal > data['balance']:
                print('Saldo anda tidak cukup')
            else:
                print(f'Anda melakukan transfer ke {target_transfer}')
                pin = input('PIN : ')
                if pin == data['pin']:
                    user["balance"] = user['balance'] - nominal
                    for user_target in all_data:
                        if user_target['id'] == target_transfer:
                            user_target['balance'] = user_target['balance'] + nominal
                            transaction_history(nominal,data['id'],target_transfer)
                else:
                    print('PIN anda salah')
        list_data.append(user)

    print() 
    system('pause')
    return to_json_by_Cy(list_data)
    
    
def transaction_history(nominal,sender,receiver):
    date = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S %p")
    history = {}
    history['date'] = date
    history['ID Sender'] = sender
    history['receiver'] = receiver
    history['nominal'] = nominal
    with open('history.json','r') as f:
        data = json.load(f)

    data.append(history)

    with open('history.json','w') as w:
        w.write(json.dumps(data,indent=4))
    